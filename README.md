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

Laranja: Muito urgente. Necessitam de atendimento praticamente imediato.

Vermelho: Emergência. Necessitam de atendimento imediato.

## Sistema de Alerta

No caso de classificação vermelha, indicando uma situação de emergência, o sistema incorpora um mecanismo de alerta, utilizando um Buzzer e uma sinalização visual. Este alerta é direcionado ao médico, proporcionando uma notificação imediata sobre a gravidade do caso. 

## Objetivo

O objetivo central do projeto é aprimorar a eficiência e a rapidez no processo de atendimento hospitalar, eliminando atrasos causados por falhas na comunicação e proporcionando uma gestão mais eficaz das prioridades de atendimento, especialmente em situações de emergência.

# _Instrução_

## Instalação
Siga estas etapas para instalar e configurar o Projeto XYZ em seu ambiente local:

1. Clone este repositório: `git clone https://github.com/seu-usuario/projeto-xyz.git`
2. Navegue até o diretório do projeto: `cd projeto-xyz`
3. Instale as dependências: `npm install` (ou `yarn install`)

## Uso
Após a instalação, você pode iniciar o Projeto XYZ usando o seguinte comando:

```bash
npm start
```

# _Códigos-fonte_

# _Esquemas eletrônicos_

# _Fluxos Node-RED_





