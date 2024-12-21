---
title: "Arroz com Feijão: A Base Nutritiva para Projetos que Funcionam"
seoTitle: "Arroz com Feijão: A Base Nutritiva para Projetos que Funcionam"
seoDescription: "O projeto que você trabalha mais parece uma sopa de letrinha? vamos falar sobre empatia!  "
datePublished: Sat Dec 21 2024 13:31:06 GMT+0000 (Coordinated Universal Time)
cuid: cm4y7wkzk003j09mt98esdsoy
slug: arroz-com-feijao-a-base-nutritiva-para-projetos-que-funcionam
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1732640097533/0bc01c75-f4d1-4aeb-9b18-b3dfc514d678.webp
tags: testing, code-quality

---

---

# Resumo

Neste artigo vamos passar literalmente pelo mínimo. Começou agora? não sabe o que o teu projeto precisa para sobreviver as alterações do dia a dia? fica comigo que a gente vai passar pelo que provavelmente ninguém vai te cobrar pra fazer, mas sério… isso é o mínimo.

---

# Só você sabe?… e talvez nem você saiba mais!

Já se deparou com a situação de ter que sustentar um produto, e ninguém sabe te dizer onde… como, e do que esse produto se alimenta?. Parece impossível né? afinal como que um sistema esta no ar e ninguém sabe de nada?. Pois então irmão, é muito mais comum do que parece.

Na rotina sufocante dos desenvolvedores é muito comum a sensação de urgência e sinceramente… se você se deixar levar por este ritmo, você vai ser engolido.

Com toda certeza, depois de tando tempo trabalhando com desenvolvimento, uma das frases que mais ouvi ao longo da minha carreira foi: “não dá tempo”, e consequentemente, pilhas e pilhas de linha de código sobem sem o mínimo de empatia para a produção. Empatia? como assim…? sim sim, empatia, tenho certeza que você não está pensando no próximo desenvolvedor que vai olhar para o código que você escreveu, e arrisco a dizer que, não pensou em você mesmo.

Meses se passaram desde o ultimo commit naquele projeto esquecido que você deu manutenção, e olha que incrível, ele deu problema, e agora? quem foi o dev que escreveu aquelas linhas de código? vixx… foi eu mesmo 😅, mas… sei lá! faz tanto tempo, nem sinto que foi eu quem escreveu aquilo 🤷, já não me reconheço mais naqueles linhas de código.

É meio louco pensar nisso, mas, sim, você já não é mais o mesmo, e naquele momento só se preocupou em entregar a solução, e muito provavel que achou completa perda de tempo investir algum tempo na documentação do projeto. Agora você se vê tendo que fazer o caminho do zero, entendendo novamente o fluxo inteiro, e tendo que investir novamente horas até chegar na solução.

A conclusão que eu cheguei com isto é, **nunca é perda de tempo investir alguns minutos dando contexto suficiente para o seu “eu” do futuro**, tenha empatia, nem que seja consigo mesmo, se é um comando, anote, coloque exemplos, explique como se estivesse explicando para uma criança, tenho certeza que você vai agradecer o seu “eu” do passado.

---

# Como sobe isso aqui?

Assim como no tópico anterior, este aqui fala um pouco sobre empatia.

Imagine-se na situação de iniciar em uma empresa, onboard vai onboard vem, e em algum momento chega até o seu computador o sistema ao qual você vai dar suporte. Uma semana se passou e você ainda não conseguiu subir o dito cujo. Não acredita?… Rede do docker?… Migrations sendo rodadas na mão? variaveis de ambientes não documentadas? falta de permissão?… Fala com um, fala com outro, cada qual te da uma fração de informação e no final do dia… ninguém sabe exatamente como que a disgraça do programa sobe do inicio ao fim.

Já passei por algumas empresas e muitas delas não investiram sequer um dia automatizando o processo de build do projeto. Este comportamento agride diretamente o tempo que um desenvolvedor começa a se tornar produtivo para a empresa, sem falar da percepção de maturidade do sistema.

A minha recomendação é: se eu demoro mais de minutos para subir um projeto, algo de errado não está certo. Atualmente existem diversas formas de automatizar o processo de build do sistema, seja através de bash scripts ou makefiles;

Como um profissional de respeito, é seu dever se preocupar com o mínimo. Como instalar e configurar o seu sistema, como usar e preferencialmente com exeplos de uso. Não esqueça que se for necessário permissões adicionais para sustentar o sistema, uma boa documentação deve ajudar o desenvolvedor, guiando ele para abertura de chamados ou aquisição das devidas permissões.

Abaixo vou deixar um exemplo de readme, ele questiona alguns pontos que vejo como interessantes quando tenho o primeiro contato com o sistema, e… só pra reforçar… é o mínimo.

**Exemplo de readme**:

```markdown
## 📝 **Descrição**

* Qual o objetivo do projeto? 
* Qual problema ele resolve? 
* Quais as principais funcionalidades?

## 🛠 **Dependencias**

* Este serviço depende de algum outro serviço ou ferramenta?
* Este serviço depende de algum cadastro em alguma plataforma ou permissão?

## 🚀 **Como rodar o projeto?**

* Quais são os passos necessários para rodar o projeto?
* Quais são as dependências necessárias? Docker? VPN? Certificado?

## 🧠 Como contribuir para o projeto?

* A branch principal é a `main`?
* Este projeto utiliza TAG's para versionamento?
* Respeitamos os testes de cobertura de código?
```

---

# Testar pra quê?

Tá… eu sei, mais um artigo falando sobre testes… mas sério, você confia no seu código? sim!? pois não deveria! Você mente pra você o tempo todo, e vai por mim, o seu código também, confiar no próprio código não é reflexo de senioridade, e sim o completo oposto, você está sendo imaturo, deixe a sindrome do corno pra trás, não seja o ultimo a saber sobre o erro que seu cógido está gerando.

Mudanças acontecem com frequencia em um código vivo, código que não muda, provavelmente ou está morto ou chegou em um nível de abstração invejável.

Testes não devem ser tratados como opcional, e sim como motivo de orgulho. Pense só… qual a melhor forma de provar que você testou?! mostrando o teste ué!. Dizer que viu funcionar em uma única execução não garante absolutamente nada.

Tem preguiça de testar?… é no mínimo estranho… pois o reflexo da falta de testes vai gerar muito mais horas de trabalho que o tempo dedicado para escrita dos testes.

Testes, acredite ou não, fazem parte do mínimo…

Vamos ver como fazer um teste, bem básico, só pra você ter uma noção do esforço. Bora lá!

Como podemos ver, o objetivo desta classe é validar se o texto informado tem palavão. O código não tem como objetivo atender questões de arquitetura de software e as melhores práticas de mercado, to tentando ser didatico ok?

```php
<?php

class BadWordsFilter
{
    private array $badWords;

    public function __construct(array $badWords)
    {
        $this->badWords = $badWords;
    }

    public function containsBadWords(string $text): bool
    {
        $wordsInText = $this->extractWords($text);

        foreach ($wordsInText as $word) {
            if ($this->isBadWord($word)) {
                return true;
            }
        }

        return false;
    }

    private function extractWords(string $text): array
    {
        // Remove caracteres especiais e retorna uma lista de palavras
        return preg_split('/\s+/', strtolower(trim(preg_replace('/[^\w\s]/', '', $text))));
    }

    private function isBadWord(string $word): bool
    {
        // Verifica se a palavra está na lista de palavras proibidas
        return in_array($word, $this->badWords, true);
    }
}
```

No teste abaixo conseguimos validar os seguintes pontos.

* Um caminho feliz, ou seja, o texto informado tem um palavrão que foi previamente mapeado.
    
* Outro caminho feliz é, o texto informado não tem palavrão
    
* O código também tem a capacidade de identificar uma palavra mesmo com letras maiusculas e minusculas.
    
* O código consegue detectar palavrão mesmo contendo caracteres especiais
    
* E o código também lida bem com textos em branco.
    

```php
<?php

use PHPUnit\Framework\TestCase;

class BadWordsFilterTest extends TestCase
{
    public function testContainsBadWordsReturnsTrueWhenTextContainsBadWord()
    {
        $filter = new BadWordsFilter(['badword', 'offensive']);

        $this->assertTrue($filter->containsBadWords('This text contains a badword.'));
    }

    public function testContainsBadWordsReturnsFalseWhenTextDoesNotContainBadWord()
    {
        $filter = new BadWordsFilter(['badword', 'offensive']);

        $this->assertFalse($filter->containsBadWords('This is a clean text.'));
    }

    public function testContainsBadWordsIgnoresCase()
    {
        $filter = new BadWordsFilter(['badword', 'offensive']);

        $this->assertTrue($filter->containsBadWords('This text contains a BADWORD.'));
    }

    public function testContainsBadWordsIgnoresSpecialCharacters()
    {
        $filter = new BadWordsFilter(['badword', 'offensive']);

        $this->assertTrue($filter->containsBadWords('This text contains a badword!'));
    }

    public function testContainsBadWordsHandlesEmptyText()
    {
        $filter = new BadWordsFilter(['badword', 'offensive']);

        $this->assertFalse($filter->containsBadWords(''));
    }
}
```

Como podemos ver, em momendo algum eu precisei testar diretamente os métodos privados, afinal, a interface pública da classe, expõe a abstração que o cliente tem interesse, os detalhes que giram em torno dessa abstração precisam ser testadas mudando o input, mas usando o mesmo método público. Então… isso significa que eu não deva testar métodos privados? Não não, segura ai… extremos são ruins, e eu evito me guiar por eles, quando eu desenvolvo, espero seguir um meio termo, e isso envolve testes também. Eventualmente um método com mais de mil linhas vai passar na sua frente e existe uma chance de ele ser privado, e antes de fazer qualquer alteração nele, comece escrevendo testes, renomeie as variaveis para algo mais palatavel e somente então, refatore.

---

# Conclusão

Obviamente muitos outros pontos são de extrema importancia para um sistema que resista as evoluções solicitadas pelo time de produto, seja eles monitoramente, entrega contínua, gestão de segredos, tratamento de erros, estratégias de backup, etc.

Tenha orgulho pelo resultado do seu trabalho, no final do dia, apensa você sabe o que você fez, e se você não se sente confortável com o que você anda fazendo, o prazer pelo seu trabalho vai ser afetado, e isto é o que eu menos desejo para você.

**Relembrando**

* Faça uma documentação, mínima que seja, dando contexto sobre o sistema
    
* Ajude você e os outros com o processo de build e up do sistema no ambiente local.
    
* Escreva testes, tá com preguiça de fazer unitário, faça de integração então, mas faça!
    

Ahhhh mas só isso não é nem o mínimo para ter um sistema top do top!. Calma dev sênior ultra mega foda das galaxias… para quem não tem nada o mínimo já é mais que d+. 😉

---

# Referências

* [https://www.gnu.org/software/bash/](https://www.gnu.org/software/bash/)
    
* [https://www.gnu.org/software/make/manual/make.html](https://www.gnu.org/software/make/manual/make.html)
    
* [https://developers.google.com/style](https://developers.google.com/style)
    
* [https://learn.microsoft.com/en-us/style-guide/welcome/](https://learn.microsoft.com/en-us/style-guide/welcome/)
    
* [https://tldp.org/](https://tldp.org/)
    
* [https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)
    
* **Tests:**
    
    * JavaScript:
        
        * [https://medium.com/easy-coding/write-test-cases-in-javascript-5c4ede800841](https://medium.com/easy-coding/write-test-cases-in-javascript-5c4ede800841)
            
        * [https://www.freecodecamp.org/news/how-to-start-unit-testing-javascript/](https://www.freecodecamp.org/news/how-to-start-unit-testing-javascript/)
            
    * Java
        
        * [https://www.freecodecamp.org/news/java-unit-testing/](https://www.freecodecamp.org/news/java-unit-testing/)
            
        * [https://dev.to/gervg/step-by-step-introduction-to-unit-testing-in-java-3ae7](https://dev.to/gervg/step-by-step-introduction-to-unit-testing-in-java-3ae7)
            
    * GO
        
        * [https://go.dev/doc/tutorial/add-a-test](https://go.dev/doc/tutorial/add-a-test)