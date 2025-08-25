import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import random

def preview_dataset():
    """Muestra una preview visual de las imágenes recolectadas"""
    
    base_path = Path("data/raw_images")
    brands = ["apple", "mcdonalds"]
    
    # Crear figura
    fig, axes = plt.subplots(2, 6, figsize=(20, 7))
    fig.suptitle('Preview del Dataset Recolectado - Apple vs McDonald\'s', fontsize=16, fontweight='bold')
    
    for brand_idx, brand in enumerate(brands):
        brand_path = base_path / brand
        images = list(brand_path.glob("*.jpg")) + list(brand_path.glob("*.png")) + list(brand_path.glob("*.jpeg"))
        
        # Tomar una muestra representativa
        sample_images = []
        
        # Intentar obtener diferentes tipos
        sizes = ['large', 'medium', 'small', 'difficult']
        for size in sizes:
            size_images = [img for img in images if size in img.name]
            if size_images:
                sample_images.extend(random.sample(size_images, min(1, len(size_images))))
        
        # Completar hasta 6 con imágenes aleatorias si es necesario
        remaining = [img for img in images if img not in sample_images]
        if len(sample_images) < 6 and remaining:
            sample_images.extend(random.sample(remaining, min(6 - len(sample_images), len(remaining))))
        
        sample_images = sample_images[:6]  # Asegurar máximo 6
        
        for img_idx in range(6):
            if img_idx < len(sample_images):
                img_path = sample_images[img_idx]
                # Cargar y mostrar imagen
                img = cv2.imread(str(img_path))
                if img is not None:
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    axes[brand_idx, img_idx].imshow(img_rgb)
                    # Extraer info del nombre
                    parts = img_path.stem.split('_')
                    size_info = parts[-1] if len(parts) >= 4 else "unknown"
                    axes[brand_idx, img_idx].set_title(f"{brand.upper()}\n{size_info}", 
                                                     fontsize=10, fontweight='bold')
                else:
                    axes[brand_idx, img_idx].text(0.5, 0.5, 'ERROR\nCargar imagen', 
                                                ha='center', va='center', fontsize=12)
                    axes[brand_idx, img_idx].set_title(f"{brand.upper()}\nERROR", fontsize=10)
            else:
                axes[brand_idx, img_idx].text(0.5, 0.5, 'Sin imagen', ha='center', va='center')
                axes[brand_idx, img_idx].set_title(f"{brand.upper()}\n-", fontsize=10)
            
            axes[brand_idx, img_idx].axis('off')
    
    plt.tight_layout()
    
    # Crear carpeta results si no existe
    Path("results").mkdir(exist_ok=True)
    
    plt.savefig('results/dataset_preview.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("✅ Preview guardado en 'results/dataset_preview.png'")
    print("🖼️  Se muestran ejemplos representativos de cada marca")

if __name__ == "__main__":
    preview_dataset()