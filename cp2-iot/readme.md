# **Detecção de Câncer de Pele com Visão Computacional**

## **Descrição**
Este projeto utiliza técnicas de visão computacional com a biblioteca **OpenCV** para detectar manchas suspeitas em imagens da pele humana. O objetivo é fornecer uma ferramenta preliminar para a detecção de possíveis sinais de câncer de pele, como melanomas. Embora o sistema não substitua diagnósticos médicos, ele pode ser uma ferramenta útil para monitoramento e análise inicial.

## **Objetivo**
Detectar características como manchas e bordas que possam indicar lesões ou alterações na pele, utilizando um dispositivo IoT (como uma câmera simples) para capturar as imagens e processá-las em tempo real.

## **Tecnologias Utilizadas**
- **OpenCV**: Para captura e processamento de imagens, como conversão para escala de cinza, aplicação de filtros e detecção de bordas.
- **Python**: Linguagem de programação utilizada para implementação do sistema.
- **Canny Edge Detection**: Técnica de detecção de bordas para identificar áreas de interesse (potenciais lesões ou manchas).

## **Requisitos**
- Python 3.x
- OpenCV: Biblioteca de processamento de imagens.
- NumPy: Biblioteca para manipulação de arrays.
- Mediatec ou similar para câmeras IoT (opcional).

## **Instalação**
Siga os passos abaixo para configurar o ambiente e rodar o projeto:

1. **Crie o arquivo do projeto.**

2. **Instale as dependências necessárias:**
   
   No terminal, execute o comando abaixo para instalar o OpenCV e NumPy:

   ```bash
   pip install opencv-python numpy
   ```

3. **Executando o código:**

   Certifique-se de que sua câmera esteja conectada ao computador (ou utilize uma webcam para testes). Depois, execute o script:

   ```bash
   python detectar_cancer_pele.py
   ```

   O código abrirá a janela com a câmera ao vivo e mostrará a detecção de bordas das imagens da pele.

## **Como Funciona**
1. **Captura de Imagem**: A imagem é capturada em tempo real através de uma câmera.
   
2. **Pré-processamento**:
   - A imagem é convertida para escala de cinza para facilitar a detecção de bordas.
   - Um filtro de suavização (Gaussian Blur) é aplicado para reduzir o ruído.

3. **Detecção de Bordas**: Usamos o **Canny Edge Detection** para detectar as bordas na imagem. O algoritmo encontra as áreas com grandes variações de intensidade, o que pode indicar a presença de uma lesão ou mancha.

4. **Exibição**: As bordas detectadas são mostradas em uma imagem binária, com as bordas em branco e o fundo em preto.

## **Exemplo de Uso**
- **Tela ao Vivo**: O sistema captura a imagem da pele e destaca as bordas de manchas suspeitas.
- **Análise Posterior**: A imagem processada pode ser salva para posterior análise e consulta a um profissional de saúde.

## **Explicação do Código**
- **Captura de Imagem**: O código usa `cv2.VideoCapture(0)` para capturar imagens em tempo real.
- **Pré-processamento**: A imagem é convertida para uma versão em escala de cinza e um filtro de suavização é aplicado para melhorar a qualidade da imagem.
- **Detecção de Bordas**: O algoritmo Canny é utilizado para identificar bordas na imagem, destacando áreas de interesse, como manchas na pele.

## **Conclusão**
Este sistema de detecção de bordas pode ser a base para um sistema mais robusto de monitoramento da pele. Em um cenário ideal, a solução pode ser expandida para identificar tipos específicos de lesões através de aprendizado de máquina ou redes neurais, ajudando no diagnóstico precoce do câncer de pele.

## **Próximos Passos**
1. Melhorar a acurácia da detecção, implementando algoritmos mais avançados de aprendizado de máquina.
2. Integrar com dispositivos IoT reais para coleta contínua de imagens.
3. Criar uma interface gráfica para interação do usuário com o sistema.

## **Autores**
- RM - 93092
- RM - 97894
- RM - 55078
