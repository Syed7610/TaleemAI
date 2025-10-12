
# Auto-generated wrapper to call functions from converted notebooks if present.
import importlib, sys
from pathlib import Path
import pandas as pd, numpy as np

_this_dir = Path(__file__).resolve().parent
if str(_this_dir) not in sys.path:
    sys.path.insert(0, str(_this_dir))

_available = {}

def _scan():
    for py in _this_dir.glob("*.py"):
        if py.name == "wrappers.py": 
            continue
        name = py.stem
        try:
            spec = importlib.util.spec_from_file_location(name, str(py))
            module = importlib.util.module_from_spec(spec)
            loader = spec.loader
            if loader:
                loader.exec_module(module)
                for fname in ["preprocess_df", "generate_recommendations", "translate_text", "analytics_summary", "load_models"]:
                    if hasattr(module, fname):
                        _available[fname] = getattr(module, fname)
        except Exception:
            pass

_scan()

def preprocess_df(df):
    if "preprocess_df" in _available:
        try:
            return _available["preprocess_df"](df)
        except Exception:
            pass
    # fallback cleaner
    out = df.copy()
    for c in out.select_dtypes(include=[np.number]).columns:
        out[c] = out[c].fillna(out[c].mean())
    for c in out.select_dtypes(include=[object]).columns:
        out[c] = out[c].fillna("")
    return out

def generate_recommendations(df):
    if "generate_recommendations" in _available:
        try:
            return _available["generate_recommendations"](df)
        except Exception:
            pass
    # fallback simple recommender
    numeric = df.select_dtypes(include=[np.number])
    if numeric.shape[1] >= 1:
        perf = numeric.mean(axis=1)
        norm = (perf - perf.min())/(perf.max()-perf.min()+1e-9)
        risk = ((1 - norm)*100).round(1)
    else:
        risk = pd.Series([50]*len(df), index=df.index)
    recs = pd.DataFrame({"index": df.index, "risk_score": risk, "recommendation": ["Targeted revision" for _ in df.index]})
    return recs

def translate_text(text):
    if "translate_text" in _available:
        try:
            return _available["translate_text"](text)
        except Exception:
            pass
    # simple fallback: return truncated text
    t = str(text or "")
    return t if len(t) <= 300 else (t[:300] + "...")

def analytics_summary(df):
    if "analytics_summary" in _available:
        try:
            return _available["analytics_summary"](df)
        except Exception:
            pass
    numeric = df.select_dtypes(include=[np.number])
    if numeric.shape[1] > 0:
        return {"describe": numeric.describe().to_dict(), "class_avg": float(numeric.mean().mean())}
    return {"note": "No numeric data for analytics."}
