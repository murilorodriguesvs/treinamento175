#!/usr/bin/python
print("Content-type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia do Gestor para a CVM 175</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Paleta de Cores Suno */
        :root {
            --suno-red: #D42126;
            --suno-gray: #4B4B4B;
            --neutral-2: #DDDDDD;
            --neutral-3: #BBBBBB;
            --neutral-5: #999999;
            --neutral-8: #666666;
            --background-light: #F7F7F7;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            overflow: hidden;
            background-color: var(--background-light);
        }
        .slide {
            display: none;
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
        }
        .slide.active {
            display: flex;
            opacity: 1;
        }
        
        /* Custom progress bar */
        .progress-bar-container {
            height: 4px;
            background-color: var(--neutral-2);
        }
        .progress-bar {
            height: 100%;
            background-color: var(--suno-red);
            transition: width 0.3s ease-out;
        }

        /* Helpers for custom colors */
        .bg-suno-red { background-color: var(--suno-red); }
        .text-suno-red { color: var(--suno-red); }
        .border-suno-red { border-color: var(--suno-red); }
        
        .text-suno-gray { color: var(--suno-gray); }
        .text-neutral-8 { color: var(--neutral-8); }
        
        .bg-neutral-2-light { background-color: #f0f0f0; }
        .border-neutral-2 { border-color: var(--neutral-2); }

        /* Style for agenda links */
        .agenda-link {
            background: none; border: none; padding: 0; font: inherit;
            color: inherit; cursor: pointer; text-align: left;
            transition: color 0.2s; text-decoration: none;
        }
        .agenda-link:hover {
            color: var(--suno-red);
        }

        /* Style for interactive cards (Hover) */
        .interactive-card {
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .interactive-card .interactive-content {
            visibility: hidden; opacity: 0; position: absolute;
            bottom: 105%; left: 0; right: 0;
            background-color: var(--suno-gray); color: white;
            padding: 1rem; border-radius: 0.5rem;
            transition: opacity 0.3s, visibility 0.3s;
            z-index: 10; font-size: 0.9rem; line-height: 1.4;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            pointer-events: none;
        }
        .interactive-card:hover .interactive-content {
            visibility: visible; opacity: 1;
        }
        .interactive-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        /* Styles for Tabs and Accordion */
        .tab-btn {
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
        }
        .tab-btn.active {
            color: var(--suno-red);
            border-bottom-color: var(--suno-red);
        }
        .tab-content {
            display: none;
        }
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out;
        }
    </style>
</head>
<body class="flex flex-col h-screen">

    <!-- Presentation Container -->
    <div id="presentation-container" class="flex-grow w-full max-w-6xl mx-auto p-4 md:p-8 flex items-center justify-center">
        <div class="aspect-video w-full bg-white rounded-xl shadow-2xl flex flex-col p-8 md:p-12 relative overflow-hidden">
            
            <!-- Slide 1: Title -->
            <div class="slide active flex-col justify-center items-center text-center">
                <div class="w-24 h-1 bg-suno-red mb-6"></div>
                <h1 class="text-4xl md:text-5xl font-bold text-suno-gray">Da norma à prática: entendendo a RCVM 175 na Gestão de Recursos</h1>
                <p class="mt-12 text-neutral-5">Como alinhar processos internos às exigências regulatórias e às melhores práticas de mercado.
</p>
                <p class="mt-4 text-2xl md:text-3xl text-suno-red">Resolução CVM 175</p>
                <p class="mt-12 text-neutral-5">Use as setas do teclado ou os botões para navegar</p>
            </div>

            <!-- Slide 2: Agenda -->
            <div class="slide flex-col justify-center">
                <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-8">Estrutura do Treinamento</h2>
                <ul id="agenda-list" class="space-y-3 text-lg text-neutral-8">
                    <li class="flex items-start"><span class="text-suno-red font-bold mr-3">1.</span><button class="agenda-link" data-target-slide="2">Introdução ao Novo Marco Regulatório</button></li>
                    <li class="flex items-start"><span class="text-suno-red font-bold mr-3">2.</span><button class="agenda-link" data-target-slide="3">Governança e Deveres Fundamentais</button></li>
                    <li class="flex items-start"><span class="text-suno-red font-bold mr-3">3.</span><button class="agenda-link" data-target-slide="4">A Nova Arquitetura dos Fundos</button></li>
                    <li class="flex items-start"><span class="text-suno-red font-bold mr-3">4.</span><button class="agenda-link" data-target-slide="5">O Novo Regime de Responsabilidade</button></li>
                    <li class="flex items-start"><span class="text-suno-red font-bold mr-3">5.</span><button class="agenda-link" data-target-slide="6">Impactos na Gestão da Carteira</button></li>
                    <li class="flex items-start"><span class="text-suno-red font-bold mr-3">6.</span><button class="agenda-link" data-target-slide="7">Transparência e Divulgação</button></li>
                    <li class="flex items-start col-span-2"><span class="text-suno-red font-bold mr-3">7.</span><button class="agenda-link" data-target-slide="8">Síntese e Recomendação</button></li>
                </ul>
            </div>

            <!-- Slide 3: Módulo 1 -->
            <div class="slide flex-col justify-between">
                <div>
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-2">Módulo 1: Introdução ao Novo Marco Regulatório</h2>
                    <p class="text-lg text-neutral-8 mb-4">A Resolução moderniza a indústria, focando em 4 pilares principais. Passe o mouse sobre os cards para mais detalhes.</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-lg w-full">
                        <div class="interactive-card bg-neutral-2-light p-4 rounded-lg relative">
                            <h3 class="font-semibold text-suno-gray">O que motivou a mudança?</h3>
                            <div class="interactive-content"><p>A CVM 175 busca modernizar a indústria, alinhando o Brasil a práticas internacionais, atraindo investidores e aumentando a eficiência e competitividade dos fundos locais.</p></div>
                        </div>
                        <div class="interactive-card bg-neutral-2-light p-4 rounded-lg relative">
                            <h3 class="font-semibold text-suno-gray">A estrutura da norma</h3>
                            <div class="interactive-content"><p>A norma é dividida em uma <strong>Parte Geral</strong>, com regras para todos, e <strong>Anexos Normativos</strong>, com regras específicas para cada tipo de fundo (FI, FIDC, FIP, etc.), facilitando a consulta.</p></div>
                        </div>
                        <div class="interactive-card bg-neutral-2-light p-4 rounded-lg relative">
                            <h3 class="font-semibold text-suno-gray">Principais conceitos</h3>
                            <div class="interactive-content"><p><strong>Fundo como condomínio:</strong> Reforça a ideia de comunhão de recursos.<br> <strong>Prestador de Serviços Essenciais:</strong> Define claramente as figuras do Administrador e do Gestor.<br> <strong>Regulamento:</strong> Torna-se a "lei" do fundo, com poder para definir até a limitação de responsabilidade.</p></div>
                        </div>
                        <div class="interactive-card bg-neutral-2-light p-4 rounded-lg relative">
                            <h3 class="font-semibold text-suno-gray">Segregação de Responsabilidades</h3>
                            <div class="interactive-content">
                                <p>Define claramente os papéis do <strong>Administrador Fiduciário</strong> (representante do fundo) e do <strong>Gestor</strong> (decisões de investimento), aumentando a governança.</p>
                                <p class="text-suno-red text-xs mt-2 font-semibold">Fonte: Resolução CVM 175, Arts. 85 e 103</p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Audio Player -->
                <div class="mt-auto pt-4 flex items-center gap-3 bg-gray-100 p-2 rounded-lg w-full max-w-lg mx-auto" style="margin-top: 5%;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--suno-gray)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3Z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v3Z"></path></svg>
                    <audio controls class="w-full h-8">
                        <source src="./Podcasts/Módulo1.mp4" type="audio/mpeg">
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                </div>
            </div>

            <!-- Slide 4: Módulo 2 -->
            <div class="slide flex-col justify-between">
                <div class="w-full">
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-4">Módulo 2: Governança e Deveres Fundamentais</h2>
                    <div id="tabs-container-module2" class="w-full">
                        <div class="border-b border-neutral-3 mb-4">
                            <nav class="flex space-x-8 -mb-px" aria-label="Tabs">
                                <button class="tab-btn active whitespace-nowrap py-3 px-1 font-medium text-lg" data-tab="1">Comunicação e Documentação</button>
                                <button class="tab-btn whitespace-nowrap py-3 px-1 font-medium text-lg" data-tab="2">Governança e Supervisão</button>
                            </nav>
                        </div>
                        <div class="w-full">
                            <div id="tab-content-module2-1" class="tab-content" style="display: block;">
                                <div class="space-y-3 text-neutral-8 text-base accordion-container">
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Encaminhar cópia de documentos ao administrador</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4"><ul class="list-disc list-inside text-sm space-y-1"><li>É recomendável criar um fluxo de trabalho para digitalizar e enviar cada documento assinado da classe de cotas, respeitando o prazo de 5 dias úteis.</li><li>Uma boa prática é designar um responsável e utilizar um checklist para o controle de prazos.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Resolução CVM 175, Art. 87</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Manter documentação das operações em ordem</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4"><ul class="list-disc list-inside text-sm space-y-1"><li>Sugerimos a implementação de um sistema de arquivamento digital (GED) com uma política clara de nomenclatura e rotinas de backup.</li><li>É fundamental garantir que todos os documentos que suportam as decisões de investimento sejam devidamente arquivados.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Resolução CVM 175, Art. 105, III e IV</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Fornecer material e informações aos distribuidores</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4"><ul class="list-disc list-inside text-sm space-y-1"><li>Uma boa prática é centralizar e padronizar o material de divulgação (lâmina, regulamento) a ser enviado aos distribuidores.</li><li>Recomendamos estabelecer um canal de comunicação formal (e-mail, portal) para notificar sobre qualquer alteração na classe, especialmente as que mudam o regulamento.</li><li>É recomendável estabelecer um controle de mudanças do regulamento, para cada fundo, para comunicação interna e dos distribuidores.</li><li>Uma boa prática é comunicar sobre a eventual existência de fundos, classes e subclasses de cotas que não estejam admitindo captação</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Resolução CVM 175, Art. 58</p></div></div>
                                    </div>
                                </div>
                            </div>
                            <div id="tab-content-module2-2" class="tab-content">
                                <div class="space-y-3 text-neutral-8 text-base accordion-container">
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Observar estritamente o regulamento</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4"><ul class="list-disc list-inside text-sm space-y-1"><li>Aconselhamos o uso de um checklist de enquadramento pré-operação para validar a aderência à política de investimento e outras regras.</li><li>É uma boa prática realizar treinamentos periódicos com a equipe sobre os regulamentos de cada fundo. O time de Compliance poderá auxiliar nos treinamentos periódicos.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Resolução CVM 175, Art. 105, V</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Fiscalizar os serviços de terceiros contratados</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4"><ul class="list-disc list-inside text-sm space-y-1"><li>Recomendamos estabelecer uma rotina de avaliação dos prestadores de serviço, identificando quaisquer falhas ou necessidade de troca, vistando a melhor qualidade da entrega.</li><li>Uma prática eficaz é definir e monitorar métricas de desempenho (SLAs) e exigir relatórios periódicos dos serviços.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Resolução CVM 175, Art. 105, VI</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Realizar KYP antes de contratar parceiros</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4"><ul class="list-disc list-inside text-sm space-y-1"><li>É uma prática essencial de governança que o processo de Know Your Partner (KYP) seja conduzido pelo time de Compliance antes da contratação.</li><li>Qualquer exceção a esta regra deve ser previamente discutida e formalmente aprovada pelo time de Compliance para mitigar riscos.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Melhor Prática de Governança e PLDFT</p></div></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Audio Player -->
                <div class="mt-auto pt-4 flex items-center gap-3 bg-gray-100 p-2 rounded-lg w-full max-w-lg mx-auto" style="margin-top: 5%;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--suno-gray)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3Z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v3Z"></path></svg>
                    <audio controls class="w-full h-8">
                        <source src="./Podcasts/Módulo2.mp4" type="audio/mpeg">
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                </div>
            </div>

            <!-- Slide 5: Módulo 3 -->
            <div class="slide flex-col justify-between">
                <div class="w-full">
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-4">Módulo 3: A Nova Arquitetura dos Fundos</h2>
                    <div class="space-y-3 text-neutral-8 text-base accordion-container w-full">
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Classes de cotas com patrimônios segregados</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Um único fundo (mesmo CNPJ) pode ter múltiplas classes de cotas, onde cada classe funciona como um patrimônio separado e independente, sem que os ativos de uma contaminem a outra.</div></div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Diferença entre Classes e Subclasses</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><strong>Classes:</strong> Possuem políticas de investimento distintas, mas mantendo-se nas mesmas categorias de fundos. <strong>Subclasses:</strong> Dentro de uma mesma classe, podem ter públicos-alvo, prazos e taxas diferentes (ex: subclasse para varejo, outra para qualificado).</div></div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Implicações práticas para a gestão</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">O gestor precisará administrar múltiplos portfólios segregados, com controles e enquadramentos independentes para cada classe, dentro da mesma estrutura jurídica.</div></div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Regras para insolvência de uma classe</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">A insolvência de uma classe de cotas não afeta as demais classes do fundo. O patrimônio da classe insolvente responderá por suas próprias obrigações, protegendo os investidores das outras classes.</div></div>
                        </div>
                    </div>
                </div>
                 <!-- Audio Player -->
                <div class="mt-auto pt-4 flex items-center gap-3 bg-gray-100 p-2 rounded-lg w-full max-w-lg mx-auto" style="margin-top: 5%;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--suno-gray)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3Z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v3Z"></path></svg>
                    <audio controls class="w-full h-8">
                        <source src="./Podcasts/Módulo3.mp4" type="audio/mpeg">
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                </div>
            </div>

            <!-- Slide 6: Módulo 4 -->
            <div class="slide flex-col justify-between">
                <div class="w-full">
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-4">Módulo 4: O Novo Regime de Responsabilidade</h2>
                    <div class="space-y-3 text-neutral-8 text-base accordion-container w-full">
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>A regra geral: responsabilidade fiduciária</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">O gestor, como fiduciário, deve sempre agir com lealdade e no melhor interesse dos cotistas. Esta é a base de sua responsabilidade.</div></div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Limitação da responsabilidade no regulamento</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">A Resolução CVM 175 permite que o regulamento limite a responsabilidade do gestor aos prejuízos que ele causar por dolo ou culpa grave, e não por erros normais de gestão.
				<div class="p-4 text-sm"><strong>Dolo:</strong> Intenção de causar o dano. <strong>Culpa Grave:</strong> Erro grosseiro, uma negligência ou imprudência que uma pessoa minimamente cuidadosa não cometeria. A definição exata será objeto de análise jurídica caso a caso.</div><br><span class="text-suno-red text-xs mt-2 font-semibold block">Referência: Art. 18</span>
				</div>
				</div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Responsabilidade por atos de terceiros</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Mesmo com a limitação, o gestor continua responsável por sua obrigação de supervisionar e fiscalizar os serviços prestados por terceiros que ele mesmo contratou.</div></div>
                        </div>
                    </div>
                </div>
                 <!-- Audio Player -->
                <div class="mt-auto pt-4 flex items-center gap-3 bg-gray-100 p-2 rounded-lg w-full max-w-lg mx-auto" style="margin-top: 5%;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--suno-gray)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3Z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v3Z"></path></svg>
                    <audio controls class="w-full h-8">
                        <source src="./Podcasts/Módulo4.mp4" type="audio/mpeg">
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                </div>
            </div>
            
            <!-- Slide 7: Módulo 5 -->
            <div class="slide flex-col justify-between">
                 <div class="w-full">
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-4">Módulo 5: Impactos na Gestão da Carteira</h2>
                    <div id="tabs-container-module5" class="w-full">
                        <div class="border-b border-neutral-3 mb-4">
                            <nav class="flex space-x-8 -mb-px" aria-label="Tabs">
                                <button class="tab-btn active whitespace-nowrap py-3 px-1 font-medium text-lg" data-tab="1">FIDCs</button>
                                <button class="tab-btn whitespace-nowrap py-3 px-1 font-medium text-lg" data-tab="2">FIIs</button>
                                <button class="tab-btn whitespace-nowrap py-3 px-1 font-medium text-lg" data-tab="3">FIAGROs</button>
                            </nav>
                        </div>
                        <div class="w-full">
                            <div id="tab-content-module5-1" class="tab-content" style="display: block;">
                                <div class="space-y-3 text-neutral-8 text-base accordion-container">
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Acompanhar o lastro dos direitos creditórios.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1"><li>Recomendamos implementar um sistema de verificação para validar a existência e titularidade dos lastros periodicamente.</li><li>Uma boa prática é manter um dossiê eletrônico para cada operação com todos os documentos comprobatórios.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Res. CVM 175, Anexo Normativo II, Art. 33</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Substituição dos direitos creditórios.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1"><li>Na hipótese de ocorrer substituição de direitos creditórios, por qualquer motivo, diligenciar para que a relação entre risco e retorno da carteira de direitos creditórios não seja alterada, nos termos da política de investimentos</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Res. CVM 175, Anexo Normativo II, Art. 33</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Controlar o fluxo de pagamentos dos direitos creditórios.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1"><li>Sugerimos a contratação de um prestador de serviço especializado (servicer) para o controle e a cobrança dos fluxos.</li><li>É aconselhável estabelecer um sistema de alertas para identificar rapidamente qualquer atraso ou default nos pagamentos.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Res. CVM 175, Anexo Normativo II, Art. 33</p></div></div>
                                    </div>
                                </div>
                            </div>
                            <div id="tab-content-module5-2" class="tab-content">
                                <div class="space-y-3 text-neutral-8 text-base accordion-container">
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Manter em ordem os títulos de propriedade dos imóveis.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1"><li>Uma boa prática é realizar auditorias imobiliárias regulares para verificar a situação legal e documental de cada imóvel.</li><li>Aconselhamos manter as matrículas e certidões atualizadas em um repositório central seguro.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Res. CVM 175, Anexo Normativo III, Art. 34</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Distribuição de rendimentos nas notas explicativas das DFs.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1">É recomendável acompanhar a inclusão das informações essenciais a serem incluídas na nota explicativa de distribuição de rendimentos dos FIIs.
</ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Ofício-Circular nº 1/2024/CVM/SSE/SNC</p></div></div>
                                    </div>
                                </div>
                            </div>
                            <div id="tab-content-module5-3" class="tab-content">
                                <div class="space-y-3 text-neutral-8 text-base accordion-container">
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Diligenciar integridade fundiária e ambiental dos imóveis rurais.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1"><li>Sugerimos incluir na análise do ativo a verificação de licenças ambientais, CAR, e ausência de embargos.</li><li>É uma boa prática utilizar ferramentas de geomonitoramento e vistorias em campo para acompanhar a conformidade.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Res. CVM 175, Anexo Normativo V, Art. 29</p></div></div>
                                    </div>
                                    <div class="accordion-item bg-neutral-2-light rounded-lg">
                                        <div class="p-3 flex justify-between items-center cursor-pointer"><span>Observar regras de FIIs, FIPs e FIDCs em certos investimentos.</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                                        <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm"><ul class="list-disc list-inside space-y-1"><li>Recomendamos criar uma matriz de conformidade que mapeie quais regras de outros anexos se aplicam ao FIAGRO.</li><li>É fundamental capacitar a equipe sobre os pontos essenciais da regulamentação de FII, FIP e FIDC.</li></ul><p class="text-suno-red text-xs mt-3 font-semibold">Fonte: Res. CVM 175, Anexo Normativo V, Art. 29</p></div></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Audio Player -->
                <div class="flex items-center gap-3 bg-gray-100 p-2 rounded-lg w-full max-w-lg mx-auto" style="margin-top: 5%;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--suno-gray)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3Z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v3Z"></path></svg>
                    <audio controls class="w-full h-8">
                        <source src="./Podcasts/Módulo5.mp4" type="audio/mpeg">
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                </div>
            </div>

            <!-- Slide 8: Módulo 6 -->
            <div class="slide flex-col justify-between">
                 <div class="w-full">
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-4">Módulo 6: Transparência e Divulgação</h2>
                    <div class="space-y-3 text-neutral-8 text-base accordion-container w-full">
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Obrigatoriedade de divulgação na internet</span><span class="text-suno-red font-bold text-sm">Como Fazer?</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Uma boa prática é definir no regulamento o canal oficial (site do gestor, adm ou fundo), além de criar um calendário de divulgação e designar um responsável pelas publicações. <br><span class="text-suno-red text-xs mt-2 font-semibold block">Referência: Art. 61</span></div></div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>A Lâmina do Fundo</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Documento padronizado e conciso, para FIFs, FIDCs e FIAGROS de Condomínio Aberto, com as principais informações do fundo (objetivo, risco, taxas, rentabilidade), que deve ser amplamente divulgado de acordo com os Suplementos indicado na Resolução CVM 175.</div></div>
                        </div>
                        <div class="accordion-item bg-neutral-2-light rounded-lg">
                            <div class="p-3 flex justify-between items-center cursor-pointer"><span>Divulgação de taxas</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                            <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">A norma exige maior transparência na divulgação da taxa de administração e de performance, incluindo o detalhamento da base de cálculo e da forma de apropriação.</div></div>
                        </div>
                    </div>
                </div>
                 <!-- Audio Player -->
                <div class="flex items-center gap-3 bg-gray-100 p-2 rounded-lg w-full max-w-lg mx-auto" style="margin-top: 5%;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--suno-gray)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-shrink-0"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3Z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v3Z"></path></svg>
                    <audio controls class="w-full h-8">
                        <source src="./Podcasts/Módulo6.mp4" type="audio/mpeg">
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                </div>
            </div>

            <!-- Slide 9: Síntese e Plano de Ação -->
            <div class="slide flex-col justify-between">
                 <div class="w-full">
                    <h2 class="text-3xl font-bold text-suno-red border-b-4 border-neutral-2 pb-2 mb-4">Módulo 7: Síntese e Recomendação</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
                        <div class="accordion-container">
                            <h3 class="text-xl font-semibold text-suno-gray mb-3">Síntese dos Pontos Críticos</h3>
                            <div class="space-y-3 text-neutral-8 text-base">
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Conhecimento do Regulamento</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">É a "lei" do fundo. Ignorá-lo pode levar a desenquadramentos, perdas financeiras e sanções. Cada decisão de investimento deve ser validada com ele.</div></div>
                                </div>
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Fluxos de Trabalho</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Processos bem definidos para comunicação e documentação não são burocracia, mas sim a principal ferramenta para mitigar erros operacionais e provar a diligência da gestão.</div></div>
                                </div>
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Supervisão de Terceiros</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">A responsabilidade final pela fiscalização de serviços contratados (consultorias, etc.) é do gestor. A culpa não pode ser terceirizada.</div></div>
                                </div>
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Documentação</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Manter tudo organizado não é apenas uma obrigação, é a sua defesa. Em uma auditoria ou questionamento, a qualidade da sua documentação será crucial.</div></div>
                                </div>
                            </div>
                        </div>
                        <div class="accordion-container">
                            <h3 class="text-xl font-semibold text-suno-gray mb-3">Recomendações</h3>
                            <div class="space-y-3 text-neutral-8 text-base">
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Revisar Regulamentos Atuais</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">O domínio de todos os regulamentos dos fundos existentes para verificar a necessidade de adaptação à CVM 175, especialmente quanto à limitação de responsabilidade.</div></div>
                                </div>
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Mapear Processos Internos</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Desenhar e formalizar os fluxos de trabalho para comunicação com o administrador, arquivamento de documentos e fiscalização de terceiros.</div></div>
                                </div>
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Revisar Contratos com Terceiros</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Verificar se os contratos com prestadores de serviço (consultores, etc.) possuem cláusulas claras de responsabilidade e métricas de desempenho (SLAs).</div></div>
                                </div>
                                <div class="accordion-item bg-neutral-2-light rounded-lg">
                                    <div class="p-3 flex justify-between items-center cursor-pointer"><span>Criar Matriz de Responsabilidades</span><span class="text-suno-red font-bold text-sm">Detalhes</span></div>
                                    <div class="accordion-content bg-white border-t border-neutral-3 rounded-b-lg"><div class="p-4 text-sm">Desenvolver um documento que atribua formalmente a cada membro da equipe a responsabilidade por cada uma das novas obrigações.</div></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
              </div>
          
            <!-- Slide 10: Dúvidas -->
            <div class="slide flex-col justify-center items-center text-center">
                 <h1 class="text-5xl font-bold text-suno-gray">Dúvidas?</h1>
                 <div class="w-24 h-1 bg-suno-red mt-6"></div>
		 <p class="text-2xl text-suno-red" style="margin-top: 10%"><a target="_blank" href="https://forms.monday.com/forms/2dbce5d6866739d0ed462baae9c70782?r=use1">Fale conosco aqui</a></p>
		 <p class="text-2xl text-suno-black" style="margin-top: 0.5%">ou</p>
		 <p class="text-2xl text-suno-red" style="margin-top: 0.5%">compliance@suno.com.br</p>
            </div>
        </div>
    </div>

    <!-- Footer with Navigation and Progress -->
    <footer class="w-full bg-white border-t border-gray-200 p-4">
        <div class="max-w-6xl mx-auto">
            <div class="flex items-center justify-between">
                <button id="prev-btn" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed">Anterior</button>
                <div class="text-sm text-gray-600">
                    Slide <span id="current-slide-num">1</span> de <span id="total-slides-num">10</span>
                </div>
                <button id="next-btn" class="px-4 py-2 bg-suno-red text-white rounded-lg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed">Próximo</button>
            </div>
            <div class="progress-bar-container mt-3 rounded-full">
                <div id="progress-bar" class="progress-bar rounded-full"></div>
            </div>
        </div>
    </footer>

    <script>
        // JavaScript for presentation logic
        const slides = document.querySelectorAll('.slide');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        const currentSlideNumEl = document.getElementById('current-slide-num');
        const totalSlidesNumEl = document.getElementById('total-slides-num');
        const progressBar = document.getElementById('progress-bar');
        const agendaList = document.getElementById('agenda-list');
        
        let currentSlide = 0;
        const totalSlides = slides.length;

        function showSlide(index) {
            slides.forEach((slide) => {
                slide.classList.remove('active');
            });
            
            const activeSlide = slides[index];
            if (activeSlide) {
                activeSlide.classList.add('active');
            }
            updateControls();
        }

        function goToSlide(index) {
            if (index >= 0 && index < totalSlides) {
                currentSlide = index;
                showSlide(currentSlide);
            }
        }

        function updateControls() {
            currentSlideNumEl.textContent = currentSlide + 1;
            totalSlidesNumEl.textContent = totalSlides;
            const progressPercentage = ((currentSlide + 1) / totalSlides) * 100;
            progressBar.style.width = `${progressPercentage}%`;
            prevBtn.disabled = currentSlide === 0;
            nextBtn.disabled = currentSlide === totalSlides - 1;
        }

        function nextSlide() {
            if (currentSlide < totalSlides - 1) {
                currentSlide++;
                showSlide(currentSlide);
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                currentSlide--;
                showSlide(currentSlide);
            }
        }

        // Event Listeners
        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') {
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                prevSlide();
            }
        });

        if (agendaList) {
            agendaList.addEventListener('click', (e) => {
                if (e.target && e.target.matches('.agenda-link')) {
                    const targetSlideIndex = parseInt(e.target.dataset.targetSlide, 10);
                    if (!isNaN(targetSlideIndex)) {
                        goToSlide(targetSlideIndex);
                    }
                }
            });
        }
        
        function setupTabs(containerId) {
            const container = document.getElementById(containerId);
            if (!container) return;

            const tabButtons = container.querySelectorAll('.tab-btn');
            
            tabButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const parentNav = button.closest('nav');
                    parentNav.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
                    button.classList.add('active');
                    
                    const tabNumber = button.dataset.tab;
                    const parentTabsContainer = button.closest('[id^="tabs-container"]');
                    parentTabsContainer.querySelectorAll('.tab-content').forEach(content => {
                        const contentIdSuffix = content.id.split('-').pop();
                        content.style.display = contentIdSuffix === tabNumber ? 'block' : 'none';
                    });
                });
            });
        }

        function setupAccordions() {
            document.querySelectorAll('.accordion-container').forEach(container => {
                container.addEventListener('click', (e) => {
                    const accordionHeader = e.target.closest('.accordion-item > div:first-child');
                    if (!accordionHeader) return;

                    const content = accordionHeader.nextElementSibling;
                    const allContentInContainer = container.querySelectorAll('.accordion-content');

                    const wasOpen = content.style.maxHeight;

                    allContentInContainer.forEach(item => {
                        item.style.maxHeight = null;
                    });

                    if (!wasOpen) {
                        const contentWrapper = content.querySelector('div');
                        content.style.maxHeight = contentWrapper.scrollHeight + "px";
                    }
                });
            });
        }
        
        setupTabs('tabs-container-module2');
        setupTabs('tabs-container-module5');
        setupAccordions();

        // Initial setup
        showSlide(currentSlide);
    </script>

</body>
</html>


""")

