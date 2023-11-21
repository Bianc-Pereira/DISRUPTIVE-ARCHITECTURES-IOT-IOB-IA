# DISRUPTIVE-ARCHITECTURES-IOT-IOB-IA
# Projeto Prontuário Dinâmico
# _Descrição_

## Introdução
O Projeto Prontuário Dinâmico foi desenvolvido pensando na otimização do tempo dentro dos hospitais. Atualmente, o prontuário médico acontece da seguinte forma na maioria dos hospitais, principalmente nos públicos:

## Triagem

O paciente chega ao hospital e passa pelo processo de triagem, onde são avaliados os sintomas, a gravidade do caso e a necessidade de atendimento imediato através das cores.
Durante a triagem, as informações básicas do paciente, como nome, idade, sexo e queixa principal, são registradas.

As informações coletadas durante a triagem são registradas no  prontuário do paciente, de forma manual e repassadas ao médico. Porém, é muito comum, os colaboradores dos hospitais se esquecerem de levar esse prontuário até o médico, ou acabar demorando, perdendo um tempo considerável.

Com isso, desenvolvemos um prontuário dinâmico, que registra todos os dados do paciente no sistema e envia pro médico de forma automática. Tais dados são: Nome, idade, gênero, nível de prioridade ( são as cores que indicam a prioridade do atendimento ). 

## Classificação das cores

Explicando melhor sobre as cores, quando o paciente recebe uma cor, significa um certo grau de prioridade no atendimento:

Azul: Não urgente. Podem aguardar atendimento ou serem encaminhados para outros serviços de saúde

Verde: Pouco urgente. Podem aguardar atendimento ou serem encaminhados para outros serviços de saúde.

Amarelo: Urgente. Necessitam de atendimento rápido, mas podem aguardar.

Vermelho: Emergência. Necessitam de atendimento imediato.

## Sistema de Alerta

No caso de classificação vermelha, indicando uma situação de emergência, o sistema incorpora um mecanismo de alerta, utilizando um Buzzer e uma sinalização visual. Este alerta é direcionado ao médico, proporcionando uma notificação imediata sobre a gravidade do caso. 

## Objetivo

O objetivo central do projeto é aprimorar a eficiência e a rapidez no processo de atendimento hospitalar, eliminando atrasos causados por falhas na comunicação e proporcionando uma gestão mais eficaz das prioridades de atendimento, especialmente em situações de emergência.

# _Instrução_

## Instalação
Siga estas etapas para instalar e configurar o Projeto Prontuário Dinâmico em seu ambiente local:

1. Faça login na sua conta WOKWI: `https://wokwi.com/projects/new/arduino-uno`

2. Monte um circuito com buzzer, led, dois resistores e um ESP32

3. Insira no campo o código fonte na pasta: `https://github.com/Bianc-Pereira/DISRUPTIVE-ARCHITECTURES-IOT-IOB-IA/blob/main/ESP32/main.py`

4. Instale as bibliotecas :
import network
import network
from machine import Pin, PWM
import dht
import ujson
from umqtt.simple import MQTTClient
import json
import time

5. Verificar se o Node esta instalado. Caso não esteja, usar o seguinte link para instalação : `https://nodejs.org/en`
6. Instalar Node-Red. Caso não esteja instalado, usar o seguinte código no cmd: `npm install -g --unsafe-perm node-red`
7. "node-red" (código para abrir o node-red)
8. Ao executar o Node-RED, abrir no navegador a porta localhost http://127.0.0.1:1880/red/
9. Inserir e debugar o seguinte flow: `https://github.com/Bianc-Pereira/DISRUPTIVE-ARCHITECTURES-IOT-IOB-IA/blob/main/Node-red/flows.json`
10. Verificar se o flow devolve a seguinte mensagem:
   
    ![Captura de tela 1](https://private-user-images.githubusercontent.com/126917573/284101942-1daf6f1e-657b-4dc3-a0e0-e4aecb82ec01.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA2MDkyMjgsIm5iZiI6MTcwMDYwODkyOCwicGF0aCI6Ii8xMjY5MTc1NzMvMjg0MTAxOTQyLTFkYWY2ZjFlLTY1N2ItNGRjMy1hMGUwLWU0YWVjYjgyZWMwMS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEyMVQyMzIyMDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZDRmMDg5YzNkNGY2ZDg4ZGJmMDgzZTkzNGMzOGI1M2IxMWE1NWZlNjdmYjBkZThlZGIwNmZhOGVlMzI2YzVlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Kz1iLllwbugbKAVs9GyWGgU_6eSpVvxlahkplLLvsjY)

11. Acompanhar no ESP32 a executação do protótipo
    `https://youtu.be/aaU7igDeAX0`



## Uso
Após a instalação, você pode iniciar o Projeto Prontuário Dinâmico usando o seguinte comando:

```bash
npm start
```

# _Códigos-fonte da função Node-RED_

![Captura de tela 1](https://private-user-images.githubusercontent.com/126917573/284101944-a4307fe6-25ee-4623-8e2d-1b8ae848dbdb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA2MDU5MjMsIm5iZiI6MTcwMDYwNTYyMywicGF0aCI6Ii8xMjY5MTc1NzMvMjg0MTAxOTQ0LWE0MzA3ZmU2LTI1ZWUtNDYyMy04ZTJkLTFiOGFlODQ4ZGJkYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEyMVQyMjI3MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NTlkMWMwYmZkZTkyMGE0YTM3MjE5NzczYjBlNGVlOTI1MDYwNDc3Y2QyZTI0MjQ3MTBmM2Y5MTc4NTRlYWY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.LuGmzSjKf50pp6PurIZ9GkmJ8iB2vuOy2Y37gmZtQN4)

# _Esquemas eletrônicos_

![Captura de tela 1](https://private-user-images.githubusercontent.com/126917573/284101920-5782c0b3-fc11-4b1a-833a-f1c42ae5aac7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA2MDU5MjMsIm5iZiI6MTcwMDYwNTYyMywicGF0aCI6Ii8xMjY5MTc1NzMvMjg0MTAxOTIwLTU3ODJjMGIzLWZjMTEtNGIxYS04MzNhLWYxYzQyYWU1YWFjNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEyMVQyMjI3MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMjgzM2E1MTY4MjRjZGNlODVhMGU4MTYxZGFkYTIxYWY5OWEzNGIzOTgzOTFiNWI1ZjQ5MzljMWIxN2VlNTRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.zEwaZBVmXt4F0MiyaIoxKN3KRyqqR1fPebCbl80iMcE)

# _Fluxos Node-RED_

![Captura de tela 1](https://private-user-images.githubusercontent.com/126917573/284101957-67bdb341-7917-4eaa-9b68-46559da78c30.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA2MDU5MjMsIm5iZiI6MTcwMDYwNTYyMywicGF0aCI6Ii8xMjY5MTc1NzMvMjg0MTAxOTU3LTY3YmRiMzQxLTc5MTctNGVhYS05YjY4LTQ2NTU5ZGE3OGMzMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEyMVQyMjI3MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lOThjMGZlM2QxYTljMDg4OTJiYThjNWMyOGFlY2M0OTRmMjlhMTM4M2MzOTY2ZmMxOTQwZGVlMWI1ZWFmNzUyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.V9yUHXoINKrz1gnp6DZ3auA-3Y6kU4Q9vdmpEaXH8DI)

# _Protótipo funcional_

https://youtu.be/aaU7igDeAX0



