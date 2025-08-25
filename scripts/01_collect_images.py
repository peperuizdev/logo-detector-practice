import os
import cv2
from pathlib import Path
import re

def verify_images():
    """Verifica que las imágenes descargadas sean válidas y sigan la convención de nombres"""
    
    base_path = Path("data/raw_images")
    brands = ["apple", "mcdonalds"]
    
    print("🔍 VERIFICANDO DATASET RECOLECTADO (2 MARCAS)")
    print("=" * 60)
    
    total_images = 0
    naming_issues = []
    
    for brand in brands:
        brand_path = base_path / brand
        
        if not brand_path.exists():
            print(f"❌ Carpeta {brand} no existe")
            continue
            
        images = list(brand_path.glob("*.jpg")) + list(brand_path.glob("*.png")) + list(brand_path.glob("*.jpeg"))
        count = len(images)
        total_images += count
        
        print(f"\n📁 {brand.upper()}: {count} imágenes")
        
        # Verificar convención de nombres
        pattern = rf"{brand}_\d{{3}}_\w+_(large|medium|small|difficult)\.(jpg|png|jpeg)"
        
        valid_names = 0
        corrupted = []
        small_images = []
        
        for img_path in images:
            # Verificar nombre
            if re.match(pattern, img_path.name):
                valid_names += 1
            else:
                naming_issues.append(f"{brand}/{img_path.name}")
            
            # Verificar que se puede cargar la imagen
            try:
                img = cv2.imread(str(img_path))
                if img is None:
                    corrupted.append(img_path.name)
                else:
                    height, width = img.shape[:2]
                    if width < 200 or height < 200:
                        small_images.append(f"{img_path.name} ({width}x{height})")
            except:
                corrupted.append(img_path.name)
        
        # Reporte por marca
        print(f"  ✅ Nombres correctos: {valid_names}/{count}")
        if corrupted:
            print(f"  ❌ Imágenes corruptas: {corrupted}")
        if small_images:
            print(f"  ⚠️  Imágenes muy pequeñas: {small_images}")
        if not corrupted and not small_images:
            print(f"  ✅ Todas las imágenes son válidas")
    
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN TOTAL: {total_images} imágenes")
    
    # Verificar meta de 36 imágenes
    if total_images == 36:
        print("🎯 ¡Perfecto! Tienes exactamente las 36 imágenes objetivo")
    elif total_images >= 30:
        print("👍 Bien, tienes suficientes imágenes para empezar")
    else:
        print("🤔 Necesitas más imágenes. Objetivo: 36 total (18 por marca)")
    
    # Reportar problemas de nombres
    if naming_issues:
        print(f"\n⚠️  PROBLEMAS DE NOMBRES ({len(naming_issues)} archivos):")
        for issue in naming_issues:
            print(f"  - {issue}")
        print("💡 Renombra siguiendo: marca_XXX_contexto_tamaño.jpg")
    else:
        print("✅ Todos los nombres siguen la convención correcta")
    
    return total_images

if __name__ == "__main__":
    verify_images()