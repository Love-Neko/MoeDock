import os
import zipfile
from pathlib import Path

def package_release():
    root = Path(__file__).resolve().parent.parent
    dist_dir = root / "dist"
    dist_dir.mkdir(exist_ok=True)
    
    zip_path = dist_dir / "MoeDock-Icons-Pack.zip"
    print(f"[Packaging] Creating release bundle: {zip_path}")
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Add PNG and ICO icons
        for category in ["PNG图标", "ICO图标"]:
            icon_dir = root / "例图" / category
            if icon_dir.exists():
                for f in sorted(icon_dir.glob("*.*")):
                    arcname = f"MoeDock-Icons/{category}/{f.name}"
                    zf.write(f, arcname)
                    print(f"  + Added: {arcname}")
                    
        # Add preview HTML and documentation
        for doc in ["dock_preview.html", "README.md", "LICENSE"]:
            doc_file = root / doc
            if doc_file.exists():
                arcname = f"MoeDock-Icons/{doc}"
                zf.write(doc_file, arcname)
                print(f"  + Added: {arcname}")

    print(f"\n[Done] Successfully built release zip: {zip_path} ({zip_path.stat().st_size / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    package_release()
