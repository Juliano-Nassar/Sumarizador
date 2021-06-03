import Methods.summarizer as summarizer

print("="*80)

file_path = input("Caminho para o arquivo: ")

print("="*80)

print("FAZENDO A LEITURA DO ARQUIVO")

with open(file_path, 'r') as file:
    org_text = file.read()

text = org_text.replace('\n', ' ')    

print("TEXTO IMPORTADO COM SUCESSO")

print("="*80)

k = int(input("Número de frases no sumário: "))

print("="*80)

print("SUMARIZANDO O TEXTO")

summary = summarizer.summarize(text,k)

print("TEXTO SUMARIZADO")

print("="*80)

print("SUMÁRIO:")

print(summary)

with open("TEXT_SUMMARY.txt","w") as f:
    f.write(summary)
    
with open("TEXT.txt","w") as f:
    f.write(org_text)