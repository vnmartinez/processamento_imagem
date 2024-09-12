from PIL import Image, ImageEnhance
import os
import time
from concurrent.futures import ThreadPoolExecutor

def processar_imagem(image_path, output_dir, size=(800, 600)):
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

def processar_imagens_concorrente(images, output_dir, num_threads=4):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda img: processar_imagem(img, output_dir), images)

output_dir = 'imagens_convertidas'
os.makedirs(output_dir, exist_ok=True)
image_dir = 'imagens_originais'
images = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('jpg', 'jpeg', 'png'))]

for num_threads in [2, 4, 8]: 
    print(f"Processamento Concorrente com {num_threads} threads")
    start_time = time.time()
    processar_imagens_concorrente(images, output_dir, num_threads=num_threads)
    end_time = time.time()
    print(f"Tempo total com {num_threads} threads: {end_time - start_time:.2f} segundos\n")
