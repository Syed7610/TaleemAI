
# Dashboard runnable script for TaleemAI (created by auto-deploy)
import io, os, pandas as pd, numpy as np
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
# Attempt to import wrappers from taleem_modules
import sys
from pathlib import Path
tm_dir = Path(__file__).resolve().parents[1] / "taleem_modules"
if str(tm_dir) not in sys.path:
    sys.path.insert(0, str(tm_dir))
try:
    import wrappers
except Exception:
    wrappers = None

# Styling (light white-blue)
display(HTML("<style> .tcard{background:#ffffff;border-radius:12px;padding:12px;margin:8px 0;box-shadow:0 2px 8px rgba(32,60,120,0.08);} .header{background:#f5f9ff;padding:12px;border-radius:10px;margin-bottom:12px} </style>"))
display(HTML("<div class='header'><h2 style='color:#1f4db7;margin:6px 0'>TaleemAI — LMS Dashboard (Teacher / Student / Parent)</h2><div style='color:#4b5563'>Light / modern white-blue theme</div></div>"))

# Widgets
role = widgets.Dropdown(options=["Teacher","Student","Parent"], value="Teacher", description="Role:")
uploader = widgets.FileUpload(accept='.csv,.xlsx', multiple=False, description='Upload CSV')
nlp_translate = widgets.Checkbox(value=True, description='Enable translation/summarize')
run_btn = widgets.Button(description='Run Pipeline', button_style='primary')
save_btn = widgets.Button(description='Save Results', button_style='success')
out = widgets.Output(layout={'border':'1px solid #e6eefc','padding':'10px'})

left = widgets.VBox([role, uploader, nlp_translate, run_btn, save_btn])
main = widgets.VBox([out])
layout = widgets.HBox([left, main], layout=widgets.Layout(align_items='flex-start'))
display(layout)

_store = {}
def run_pipeline(b):
    with out:
        clear_output()
        print("Running pipeline for role:", role.value)
        df = None
        if uploader.value:
            uploaded = list(uploader.value.values())[0]
            name = uploaded['metadata']['name']
            content = uploaded['content']
            bio = io.BytesIO(content)
            try:
                if name.lower().endswith('.csv'): df = pd.read_csv(bio)
                else: df = pd.read_excel(bio)
                print(f"Loaded uploaded file: {name} ({df.shape[0]} rows)")
                # Save to repo/data/
                repo_data_dir = Path(__file__).resolve().parents[1] / "data"
                repo_data_dir.mkdir(parents=True, exist_ok=True)
                save_path = repo_data_dir / name
                df.to_csv(save_path, index=False)
                print("Saved uploaded file to:", save_path)
            except Exception as e:
                print("Failed to load uploaded file:", e)
                return
        else:
            # try to load sample from repo/data/sample.csv
            sample = Path(__file__).resolve().parents[1] / "data" / "sample.csv"
            if sample.exists():
                df = pd.read_csv(sample)
                print("Loaded sample data:", sample.name)
            else:
                print("No upload and no sample.csv present. Create/upload one and run again.")
                return

        # Preprocess
        try:
            df = wrappers.preprocess_df(df)
            print("Applied preprocess_df() from wrappers.")
        except Exception:
            print("Used default preprocessing.")

        display(df.head(5))

        # Role-specific output
        if role.value == "Teacher":
            print("\\n--- Teacher Overview ---")
            try:
                analytics = wrappers.analytics_summary(df)
                print("Analytics summary:", analytics)
            except Exception:
                print("Fallback analytics:")
                display(df.describe(include='all'))
            try:
                recs = wrappers.generate_recommendations(df)
                print("\\nTop recommendations (sample):")
                display(recs.head(10))
            except Exception:
                print("No recommendations function available. Fallback shown above.")
        elif role.value == "Student":
            print("\\n--- Student View ---")
            display(df.head(10))
            try:
                recs = wrappers.generate_recommendations(df)
                if 'index' in recs.columns:
                    recs = recs.set_index('index')
                idx = df.index[0]
                if idx in recs.index:
                    print("Your recommendations:")
                    display(recs.loc[[idx]])
            except Exception:
                pass
        else:
            print("\\n--- Parent Snapshot ---")
            display(df.head(5))
            try:
                recs = wrappers.generate_recommendations(df)
                display(recs.sort_values('risk_score', ascending=False).head(5))
            except Exception:
                pass

        # NLP / translate demonstration (sample)
        if nlp_translate.value:
            textcol = None
            for c in df.columns:
                if df[c].dtype == object and df[c].astype(str).str.len().mean() > 10:
                    textcol = c
                    break
            if textcol:
                sample_text = " ".join(df[textcol].astype(str).head(3).tolist())
                try:
                    translated = wrappers.translate_text(sample_text)
                    print("\\n--- NLP / Translation sample ---")
                    print(translated)
                except Exception:
                    print("\\nNLP translate not available.")
        # save processed results
        results_dir = Path(__file__).resolve().parents[1] / "results"
        results_dir.mkdir(parents=True, exist_ok=True)
        out_file = results_dir / f"processed_{int(time.time())}.csv"
        df.to_csv(out_file, index=False)
        print("\\nSaved processed results to:", out_file)
        _store['last_results'] = str(out_file)

run_btn.on_click(run_pipeline)

def save_results(b):
    with out:
        if 'last_results' in _store:
            print("Last processed results saved at:", _store['last_results'])
        else:
            print("No processed results to save. Run pipeline first.")
save_btn.on_click(save_results)
