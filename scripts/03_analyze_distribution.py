from pathlib import Path
from collections import defaultdict, Counter
import re

def analyze_distribution():
    """Analiza la distribución detallada del dataset"""
    
    base_path = Path("data/raw_images")
    brands = ["apple", "mcdonalds"]
    
    print("📊 ANÁLISIS DETALLADO DE DISTRIBUCIÓN")
    print("=" * 70)
    
    total_all = 0
    
    for brand in brands:
        print(f"\n🏷️  ANÁLISIS DE {brand.upper()}")
        print("-" * 50)
        
        brand_path = base_path / brand
        if not brand_path.exists():
            print(f"❌ Carpeta {brand} no encontrada")
            continue
            
        images = list(brand_path.glob("*.jpg")) + list(brand_path.glob("*.png")) + list(brand_path.glob("*.jpeg"))
        total_brand = len(images)
        total_all += total_brand
        
        # Analizar por tamaños
        sizes = defaultdict(int)
        contexts = defaultdict(int)
        
        for img_path in images:
            name = img_path.stem
            
            # Extraer tamaño (último elemento después del último _)
            if '_' in name:
                size = name.split('_')[-1]
                sizes[size] += 1
                
                # Extraer contexto (penúltimo elemento)
                parts = name.split('_')
                if len(parts) >= 3:
                    context = parts[-2]
                    contexts[context] += 1
        
        # Mostrar distribución de tamaños
        print("📏 DISTRIBUCIÓN POR TAMAÑO:")
        target_sizes = {'large': 6, 'medium': 6, 'small': 4, 'difficult': 2}
        
        for size, target in target_sizes.items():
            actual = sizes.get(size, 0)
            status = "✅" if actual >= target else "⚠️" if actual > 0 else "❌"
            print(f"  {size.capitalize()}: {actual}/{target} {status}")
        
        print(f"\n🎯 DISTRIBUCIÓN POR CONTEXTO:")
        # Mostrar contextos más comunes
        context_counts = Counter(contexts)
        for context, count in context_counts.most_common():
            print(f"  {context}: {count} imágenes")
        
        print(f"\n📈 TOTAL {brand.upper()}: {total_brand} imágenes")
        
        # Verificar si cumple objetivo
        if total_brand == 18:
            print("🎯 ¡Perfecto! Cumple objetivo de 18 imágenes")
        elif total_brand >= 15:
            print("👍 Suficientes imágenes para entrenar")
        else:
            print(f"⚠️  Necesitas {18 - total_brand} imágenes más")
    
    print(f"\n" + "=" * 70)
    print(f"🎯 RESUMEN GENERAL")
    print(f"Total imágenes: {total_all}")
    print(f"Objetivo: 36 imágenes")
    
    if total_all == 36:
        print("🎉 ¡PERFECTO! Dataset completo y balanceado")
    elif total_all >= 30:
        print("👍 Dataset suficiente para comenzar entrenamiento")
    else:
        print(f"⚠️  Faltan {36 - total_all} imágenes para completar objetivo")
    
    return total_all

if __name__ == "__main__":
    analyze_distribution()