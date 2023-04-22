import pikepdf
from tqdm import tqdm
import time

loop = tqdm(total=999, position=0, leave=False)
start_time = time.time()


for counter in range(0,999):
    try:
        pikepdf.Pdf.open('doc.pdf', password=str(counter).zfill(3))
        print('Senha: '+ str(counter).zfill(3))
        print()
        break
    except:
        loop.update(1)

print('Tempo: '+ str(time.time() - start_time))
