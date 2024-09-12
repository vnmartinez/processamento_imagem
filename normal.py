from PIL import Image, ImageEnhance
import os
import time

def processar_imagens(image_path, output_dir, size=(800, 600)):
    try:
        img = Image.open(image_path)
        img_resized = img.resize(size)
        img_bw = img_resized.convert("L")
        enhancer = ImageEnhance.Contrast(img_bw)
        img_contrast = enhancer.enhance(2.0)  
        image_name = os.path.basename(image_path)
        img_contrast.save(os.path.join(output_dir, f"processed_{image_name}"))
    
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")

output_dir = 'imagens_convertidas'
os.makedirs(output_dir, exist_ok=True)

image_dir = 'imagens_originais'
images = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('jpg', 'jpeg', 'png'))]

start_time = time.time()
for image in images:
    processar_imagens(image, output_dir)

end_time = time.time()
print(f"Tempo total da versão sequencial: {end_time - start_time:.2f} segundos")
