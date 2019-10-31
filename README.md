# homecontrol imagined and made by a Portuguese.

This is a simple home automation project where I used Raspberry PI, ESP modules, sensors and relays.

I've always wanted to have a "house of the future" but domotics is very expensive, so I decided to do something using my imagination.
I started by looking for something already done on the Internet, I quickly realised that everything that was there was not made to share and was extremely complex. I gathered bases and started to do something simple that anyone can use and do.

____________________

> Este é um projeto simples de automação doméstica onde eu usei o Raspberry PI, módulos ESP, sensores e relés.
>
>Desde sempre quis ter uma "casa do futuro" mas a domótica é muito cara, então decidi fazer algo usando a minha imaginação.
>Comecei por procurar algo já feito na Internet, rapidamente percebi que tudo o que existia não era feito para partilhar e extremamente completo. Reuni bases e comecei eu a fazer algo simple e que qualquer pessoa possa utilizar e fazer.
____________________
The beginning of everything, my main concept:
- --(5V or OS command)--> [ Raspbery PI GPIO ]--(5V)--> [ Relay board ]--> Activate Something :)
- Apache2 serves -> Python Script -> Receives GPIO Trigger -> GPIO send 5V -> Relay board -> #magic

> O início de tudo, o meu principal conceito:
> - --(5V ou comando OS )--> [ Raspbery PI GPIO ]--(5V)--> [ Relay board ]--> Activa alguma coisa :)
> - Apache2 serve -> Python Script -> recebe GPIO Trigger -> GPIO envia 5V -> Relay board -> #magia
____________________
#Linux #Bash #Python3 #Apache2 #HTML5
#OpenSource
