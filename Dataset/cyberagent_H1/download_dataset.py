from huggingface_hub import snapshot_download

print("Starte Download des FFHQ-Makeup Datasets...")
snapshot_download(
    repo_id="cyberagent/FFHQ-Makeup",
    repo_type="dataset",
    local_dir="./FFHQ-Makeup"
)
print("Download erfolgreich abgeschlossen!")
