# Conceitos básicos

- Sistema de computação: hardware + software
- Hardware: circuitos eletrônicos e periféricos eletro-óptico-mecânicos.
- Por circuitos eletrônicos entenda: processador, memória, portas de entrada/saída, etc.
- Por periféricos ... entenda: teclados, mouses, discos rígidos, unidades de disquete, CD ou DVD, dispositivos USB, etc.
- Software de aplicação -> programas destinados ao usuário do sistema. Editores de texto, navegadores, jogos, etc.
- SO é uma camada multifacetada e complexa entre aplicativos e hardware.

_Neste capítulo veremos quais os objetivos básicos do sistema operacional,
 quais desafios ele deve resolver e 
 como ele é estruturado para alcançar seus objetivos._

## 1.1 Objetivos

- Torna-se desejável oferecer aos programas aplicativos uma forma de acesso homogêna aos dispositivos físicos,
  que permita abstrair as diferenças tecnológicas entre eles.
- SO incorpora aspectos de baixo nível (como drivers de dispostivos e gerência de memória física)
  e de alto nível (como programas utilitários e a pŕopria interface gráfica).
- Palavras-chave: **abstração** e **gerência**.

### 1.1.1 Abstração de recursos

- SO deve definir interfaces abstratas para os recursos do hardware, visando atender os seguintes objetivos:
  - Prover interfaces de acesso aos dispositivos, mais simples de usar que as interfaces de baixo nível.
    - Exemplo: arquivo.
  - Tornar os aplicativos independentes do hardware.
    - Exemplo: editor de textos vs tecnologia do disco rígido.
  - Definir interfaces de acesso homogêneas para dispositivos com tecnologias distintas.	
    - Exemplo: acesso a arquivos e diretórios vs estrutura real de armazenamento dos dados.

### 1.1.2 Gerência de recursos

- Em um sistema com várias atividades simultâneas, podem surgir conflitos no uso do hardware,
  quando dois ou mais aplicativos precisam dos mesmos recuros para poder executar.
- _Políticas_ para gerenciar o uso dos recuros de hardware pelos aplicativos precisam ser definidas pelo SO,
  tal que eventuais disputas e conflitos sejam resolvidos.
- Exemplos de situações conflituosas:
  - Menos processadores que número de tarefas em execução. O mesmo para RAM.
  - Impressora deve ser usada de forma exclusiva. _Print jobs_.
  - _DoS - Denial of Service_. Sevidor forçado a dedicar seus recursos a atender um determinado usuário, em detrimento dos demais.
- SO visa abstrair o acesso e gerenciar os recursos de hardware.
- Aplicativos possuem um ambiente de execução abstrato.
- Acesso aos recursos se faz através de interfaces simples--independentes dos detalhes de baixo nível.

_Fim às 22h04._

## 1.2 Tipos de sistemas operacionais [14:55;2511]

- SOs podem ser classificados segundo diversos parâmetros e perspectivas, como:
  - Batch (de lote): _fila de execução; processamento sem interação direta com usuário._
  - De rede: _suporte à op. em rede; disp. de recursos locais à rede._
  - Distribuído: _recursos disponíveis globalmente, de forma transparente._
  - Multiusuário: _suporte à identificação de "dono" de recurso; impõe regras de controle de acesso._
  - Desktop: _voltado ao antedimento do usuário... para realização de atividades corriqueiras._
  - Servidor: _permitir gestão eficiente de grande quantidades de recursos, impondo prioridades e limites sobre seu uso; sup. à rede e multiusuários._
  - Embarcado: _construído para operar sobre hardwares de pouco recursos._
  - Tempo real: _característica essencial é previsibilidade (tempo de resposta conhecido no melhor e pior caso); pode ser *soft* ou *hard* real-time system._
 
## 1.3 Funcionalidades

- A abstração e gerência de recursos depende das exigências específicas destes.
- Gerência do processador (ou de processos): _distribuição da capacidade de processamento de forma justa (não igual) entre as aplicações;
  abstrações para sincronizar atividades interdependentes; prover formas de comunicação entre si._
- Gerência de memória: _cada aplicação tem sua área de memória--independente e isolada;
  isolamento implica em estabilidade e segurança; **memória virtual** é uma abstração que desvincula os endereços de memória
  vistos por cada aplicações dos endereços acessados pelo processador na RAM._
- Gerência de dispositivos: _implementa a interação com cada dispositivo por meio de **drivers**; 
  cada periférico tem seus detalhes; periféricos similares compartilham abstrações similares--mesma interface de acesso._ 
- Gerência de arquivos: _construída sobre a gerência de dispositivos; define a abstração, interface de acesso e as regras para o uso de arquivos e diretórios._
- Gerência de proteção: _protege os recuros do sistema contra acessos indevidos; definição de usuários e grupos, identificação/autenticação dos usuários;
  definição e aplicação de regras de controle de acessos aos recursos, autorização; registro do uso de recursos, auditoria e contabilização._
- Interface gráfica, suporte de rede, fluxos de multimída, gerência de energia etc., se agregam aos sistemas modernos, complementando-os.
- São interdependentes.
- Regra importante: **política != mecanismo**.
  - Política: _aspectos de decisão mais abstratos._
  - Mecanismos: _procedimentos de baixo nível usados para implementar as políticas._
- Mecanismos devem ser suficientemente genéricos.

_Fim às 15:30_

