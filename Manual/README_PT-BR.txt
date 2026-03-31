============================================================================
  Evi Portable — Manual do usuário (visão geral)
  Documento: Inglês • Aplica-se à compilação que você recebeu com esta pasta
============================================================================

Coloque aqui também seus próprios guias mais longos ou traduções (por exemplo, EN_User_Manual.pdf,
DE_Handbuch.txt). Este arquivo é opcional para a execução do Evi; é para você ler
ou imprimir.

Cópias localizadas: README_<LANG>.txt e FEHLERSUCHE_<LANG>.txt nesta pasta
(mesmos códigos de idioma da interface do site). Visão geral em inglês: este README.txt;
Solução de problemas em inglês: FEHLERSUCHE_EN.txt. A solução de problemas alemã também é
mantido manualmente como FEHLERSUCHE_DE.txt.

Índice de pasta (nomeação de arquivo, gerador): README.md

--------------------------------------------------------------------------------
  Sistema operacional
--------------------------------------------------------------------------------

Evi Portable é apenas para Microsoft Windows 10 e Windows 11. Não é
compatível com Windows 7/8, macOS, Linux ou sistemas operacionais móveis.

--------------------------------------------------------------------------------
  Primeira inicialização – desde o download até a execução do Evi
--------------------------------------------------------------------------------

1) Local de instalação
   Copie ou extraia toda a pasta Evi para um local que você controle – por exemplo
   sua área de trabalho, documentos ou um pendrive. Mantenha a estrutura de pastas como
   entregue (não exclua subpastas que você mesmo não criou).

2) Modelo de linguagem (obrigatório)
   Evi precisa de um arquivo principal de modelo de IA (extensão .gguf) na pasta:
   modelos\llm\
   Consulte models\llm\README.txt para recomendações de tamanho. Depois que o arquivo estiver lá,
   inicie Evi; ele detecta o modelo automaticamente quando possível.

3) Primeiro lançamento – ativação
   Ao iniciar o Evi pela primeira vez, uma janela de ativação será exibida.
   • Seu PC mostra uma ID de máquina (exclusiva para este hardware).
   • Copie o ID da Máquina (botão: “Copiar ID da Máquina”) e envie por e-mail para:
     Brielbeck@hotmail.de
   • Você receberá uma chave serial que funciona apenas no mesmo PC
     (a chave está vinculada ao seu hardware).
   • Cole a chave na janela de ativação e escolha Ativar.

   Se você alterar o hardware principal ou mover o disco de uma forma que altere o ID,
   você pode precisar de uma nova chave – entre em contato com o mesmo endereço.

4) Após a ativação
   A janela principal é aberta. Escolha idioma, microfone e voz à esquerda
   painel de configurações. Diga "abrir a folha de dicas" a qualquer momento para obter exemplos de comandos
   (veja cheatsheets\en.txt e arquivos irmãos para outros idiomas).

5) Opcional: abra este manual no Windows
   No File Explorer vá para a pasta Evi, depois Manual\README.txt, e abra-o
   com o Bloco de Notas ou qualquer visualizador de texto.

--------------------------------------------------------------------------------
  Linguagem de interface (GUI)
--------------------------------------------------------------------------------

A interface do usuário segue o idioma que você escolher em Idioma na parte superior
do painel de configurações esquerdo (primeiro bloco na barra lateral). Depois de selecionar um
idioma, menus, botões, rótulos e a maior parte do texto na tela mudam para esse
idioma onde quer que existam traduções. Você pode alterá-lo a qualquer momento; apenas o
o texto muda, não o layout.

Dica: As folhas de dicas de comando na pasta cheatsheets\ são listadas por
código do idioma (en.txt, de.txt,…). Para obter detalhes, consulte cheatsheets\README.txt.
Esta pasta Manual\ é a visão geral mais longa do produto; folhas de dicas são as
lista rápida de "o que dizer".

--------------------------------------------------------------------------------
  Placa gráfica (GPU) — guia rápido
--------------------------------------------------------------------------------

Uma escolha intermediária forte é uma NVIDIA GeForce RTX 4070 Ti com 12 GB de vídeo
memória: bom equilíbrio entre velocidade, tamanho do contexto e espaço para modelos maiores.

Placas de RTX 3060 a RTX 5090 podem funcionar bem; o melhor ajuste depende
em RAM, CPU, resfriamento e qual arquivo de modelo você instala. Use a predefinição de GPU em
Barra lateral do Evi para combinar com seu hardware.

Executar apenas na CPU (as predefinições "CPU… GB RAM") é uma alternativa de emergência:
O Evi permanece utilizável sem uma placa gráfica adequada, mas as respostas são muito mais lentas.
Prefira uma GPU real sempre que puder.

--------------------------------------------------------------------------------
  Totalmente portátil — quando você precisa da Internet
--------------------------------------------------------------------------------

O Evi foi desenvolvido para ser portátil: copie a pasta inteira para outra unidade, pendrive,
ou PC e inicie-o aí. Bate-papos, memórias, configurações, dados de segurança e seus
arquivo de ativação normalmente fica dentro dessa pasta (a ativação está vinculada ao
PC, não o caminho da pasta).

A Internet é principalmente para coisas que você escolhe baixar (arquivos de modelo, arquivos opcionais
vozes ou extras, atualizações) e para recursos opcionais como pesquisa na web, e-mail,
streaming ou clima quando você permite o acesso à rede.

Bate-papo principal, memória, notas, cronômetros, ferramentas de arquivo dentro de sua pasta permitida, local
reconhecimento de fala, saída de voz local e bloqueio de privacidade executados em seu
máquina sem enviar suas conversas para um serviço de nuvem. Opcional on-line
os recursos só são executados quando o acesso à rede está ativado e você os utiliza.

--------------------------------------------------------------------------------
  Segurança: PIN e desbloqueio por voz (anti-cópia)
--------------------------------------------------------------------------------

Evi pode usar um PIN de segurança e registro de voz opcional em seu dispositivo.

Quando o desbloqueio por voz é usado, cada tentativa pode solicitar um pequeno conjunto de palavras aleatórias
isso muda sempre - nem uma frase fixa para sempre. Isso bloqueia o fácil
truque de reproduzir uma única gravação antiga de sua voz. Seu PIN permanece um
linha de defesa separada.

O objetivo é impedir o abuso casual; nenhum produto de consumo pode prometer
perfeição contra todos os ataques (por exemplo, alguém que tenha seu PIN e
mimetismo de voz sofisticado). Mantenha seu PIN privado e conclua a configuração como
aplicativo orienta você.

--------------------------------------------------------------------------------
  Solução de problemas (pequena lista de verificação)
--------------------------------------------------------------------------------

• Nenhuma resposta de IA/erro de modelo
  → Pelo menos um .gguf adequado em models\llm\ ? Consulte modelos\llm\README.txt.
  → Experimente um modelo menor ou uma predefinição de CPU na barra lateral se o caminho da GPU falhar.

• Sem microfone
  → Configurações de som do Windows: teste o microfone. No Evi, escolha o dispositivo em
    Microfone e Salvar.

• Sem saída de voz
  → Verifique se os arquivos de voz do seu idioma existem na pasta piper\ e
    escolha uma voz na barra lateral.

• Web ou YouTube falham
  → Desative "Bloquear todo o tráfego" na barra lateral se desejar recursos online.
  → Para reprodução no YouTube, geralmente é necessário VLC Portable e acesso à rede.

• Depois de editar as folhas de dicas
  → Reinicie o Evi para que todos os auxiliares de texto captem as alterações de maneira confiável.

--------------------------------------------------------------------------------
  Solução de problemas (referência estendida)
--------------------------------------------------------------------------------

Verificações rápidas (sempre primeiro)
  • Windows 10 ou 11 de 64 bits, atualizado e reiniciado após grandes mudanças?
  • Evi sendo executado a partir de uma pasta totalmente extraída — e não de dentro de um arquivo?
  • Evite pastas sincronizadas na nuvem (OneDrive, etc.) para a pasta de dados ativos enquanto
    Evi é executado — use um caminho local como C:\EviPortable ou D:\Tools\Evi quando
    possível.
  • Espaço livre em disco suficiente para o modelo, chats e atualizações?
  • Após alterar modelos, vozes ou folhas de dicas: saia completamente do Evi e inicie
    novamente.

1) Sistema operacional
  • Evi é apenas para Windows 10 e 11; outras versões do sistema operacional não são suportadas.
  • Se o aplicativo não iniciar, extraia totalmente o pacote e verifique o antivírus
    logs para executáveis bloqueados e tente um caminho de instalação mais curto sem raro
    Caracteres somente Unicode.

2) Caminho da pasta, antivírus, portabilidade
  • Adicione uma exclusão para sua pasta raiz Evi no software de segurança se as varreduras fizerem
    inicialização muito lenta ou bloqueio de arquivos durante downloads.
  • Pendrives: prefira USB 3 + NTFS; mídia muito lenta torna os modelos grandes dolorosos.

3) Modelo de linguagem (.gguf)
  • sintomas: ausência de respostas, erros de modelo, falha instantânea no carregamento.
  • correções: verifique se models\llm\ contém um .gguf completo (não 0 bytes); baixar novamente
se necessário; combine o tamanho do modelo com VRAM usando models\llm\README.txt; se não tiver certeza,
    mantenha um único arquivo q4_k_m testado na pasta.
  • vários arquivos .gguf: Evi pode escolher o maior que cabe na sua VRAM — se você
    suspeitar de um conflito, teste com apenas um arquivo.

4) GPU, CUDA, drivers, falta de memória
  • Atualize o driver NVIDIA; em laptops, force a GPU / desempenho discreto
    modo para Evi onde o Windows permitir.
  • Se você observar falhas de OOM ou de GPU, use um ponto de verificação menor, feche outros aplicativos de GPU,
    temperatura mais baixa ou mude para uma predefinição de CPU (mais lenta, mas mais estável).

5) Modo somente CPU
  • Espera-se que seja lento; libere RAM de sistema suficiente; feche tarefas pesadas em segundo plano;
    use o plano de energia "Alto desempenho" durante sessões longas.

6) Ativação
  • Cole as chaves com cuidado (sem espaços extras); as chaves estão vinculadas a uma ID de máquina.
  • Após grandes alterações de hardware, você pode precisar de uma chave de substituição — use o suporte
    endereço com seus dados.

7) Microfone
  • Privacidade do Windows → Microfone → permitir aplicativos de desktop.
  • Defina o dispositivo de gravação padrão correto; no Evi escolha o mesmo dispositivo e salve.
  • Os fones de ouvido Bluetooth podem adicionar latência — teste com um microfone USB se não tiver certeza.
  • Outro aplicativo pode manter o modo exclusivo – feche o software de reunião temporariamente.

8) Reconhecimento de fala (local)
  • Se o reconhecimento nunca terminar, certifique-se de que os arquivos de modelo em models\whisper sejam
    intacto e permitir a rede nas primeiras buscas de modelo se sua construção precisar.

9) Saída de voz (Piper / TTS)
  • Confirme se o piper contém um pacote de voz para o idioma da sua UI; escolha uma voz
    a barra lateral; verifique o mixer de volume do Windows – o Evi pode ser silenciado por aplicativo.

10) Rede e “Bloquear todo o tráfego”
  • Desative o bloqueio para web, ajudantes de e-mail, previsão do tempo ou downloads.
  • Proxies corporativos ou VPNs podem exigir ajuda de TI para listas de permissões.

11) YouTube e mídia
  • Mantenha o layout VLC Portable incluído; habilitar o acesso à rede; leia
    Orientação Portable\VLCPortable se o caminho foi movido.

12) Linguagem da interface do usuário e folhas de dicas
  • As folhas de dicas estão por arquivo de idioma em cheatsheets\ — veja cheatsheets\README.txt.
  • Salvar edições como UTF-8; reinicie o Evi após as edições.

13) Segurança (PIN / desbloqueio por voz)
  • Utilize um ambiente silencioso; verifique novamente o ganho do microfone; nunca compartilhe seu PIN.
  • Os prompts de palavras aleatórias são intencionais – gravações de voz antigas não devem ser desbloqueadas.

14) Desempenho, travamentos, travamentos
  • Reduza o tamanho do modelo, melhore o resfriamento, leia qualquer crash.log na árvore se o seu
    build cria um e reverte a última alteração feita antes das falhas.

15) Ao entrar em contato com o suporte
  • Inclui Machine ID, versão Windows, modelo GPU + VRAM + driver, que .gguf
    você usa e o texto exato do erro (não as chaves secretas).

Referência completa de solução de problemas (este idioma): Manual\FEHLERSUCHE_PT-BR.txt

--------------------------------------------------------------------------------
  Suporte — chaves seriais e ID de máquina
--------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Sempre inclua sua ID de máquina na tela de ativação ao solicitar uma
chave serial ou uma chave de substituição após alterações de hardware.

============================================================================