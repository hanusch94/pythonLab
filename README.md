# pythonLab

A pyhonLab egy középiskolai informatikai szakkörhöz készült jegyzet.

# Letöltés Zip-ként:
Code alatt le tudjuk tölteni a download zip-pel.
![image](https://user-images.githubusercontent.com/13373740/165831894-aa912a89-c738-46cd-89c1-b6d040e631a8.png)

# GIT TUTORIAL
## Motiváció
Amikor többen fejlesztünk egy kódrészletet, az egyik legbonyolultabb pont, hogy hogyan egységesítsük a változtatásainkat. Erre egy megoldás a git. A cél, hogy egy feladat lefejlesztése után ne az egész kódot töltsük fel, hanem csak a változtatásokat. Így még ha egy fájlt is érintettek változások, akkor is össze tudjuk hasonlítani a módosításokat és viszonylag gyorsan össze tudjuk rakni a végleges megoldást.
Ez a téma először macerásnak tűnhet viszont minden cégnél így oldják meg, hogy párhuzamosan tudjanak egy kódon dolgozni, ezért mindenképp érdemes megismerni. Ha ezt kihagynánk, akkor a zip megoldás lehet számunkra, ám így nem tudjuk összehúzni a szerver és a saját gépen lévő változtatásainkat.

## Az alkalmazás első verziójának a leszedése
### Visual Studio Code (később VS Code)
Ez az alkalmazás a microsoft scriptelésre(rövidebb speciális célra készült programok) ajánlott alkalmazása. Maga az alkalmazás is ingyenes és a hozzá tartozó extension-ök (kiegészítők) is.
Ebben a pontban lépésről lépésre le van írva, hogyan tudjuk előkészíteni a VS Code-ot a tanuláshoz és a kényelmes munkához.
- Töltsük le a programot: https://code.visualstudio.com/download
- Telepítsük fel
- Az alkalmazást megnyitva telepítsünk 3 extensiont:
- - Egy extension telepítéséhez baloldalt válasszuk ki az extensions csempét, keressünk rá a kívánt extensionre, majd ha megtaláltuk, a listán az Install gomb megnyomásával tudjuk telepíteni. Ezt követően az alkalmazás telepíteni fogja az extensiont. (Ez nem a leg látványosabb, így várnunk kell valamennyit)
- - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166009165-973970df-138e-4344-9bea-96903102d9c3.png)
- - Python ![image](https://user-images.githubusercontent.com/13373740/166008407-df44f01a-75a1-4633-b337-c534ad86bc04.png)
- - Jupyter ![image](https://user-images.githubusercontent.com/13373740/166008840-80c634de-3b9e-4c1e-a89c-7c85385f46c3.png)
- - Git Lens ![image](https://user-images.githubusercontent.com/13373740/166008995-3ed6456c-d0c5-4c57-9ed4-f73471b8aca2.png)
- Miután megnyitunk egy jupyter dokumentumot (pl a jegyzet) a sorok futtatásához kérni fog egy python telepítést. (Az extension a parancsok felismeréséért és a kényelmes kódolásért felel. Az ezen a ponton telepített python a kód futtathatóságáért)

## Első verzió letöltése gittel
Akit részletek érdekelnének a gitről, itt van egy angol nyelvű leírás hozzá: https://www.w3schools.com/git/default.asp?remote=github
Az itteni leírásban csak az itt szükséges szintet nézzük. A későbbiekben a szakkörön szó lesz a gitről, lesz jegyzet is belőle magyar nyelven.
- Regisztráljunk gitre
- Jelentkezzünk be gitre
- A giten a projekten belül a code fülre navigáljunk
- Itt kattintsunk a bejelölt Codeˇ gombra
- Válasszuk a HTTPS-t
- A linket a mellette lévő gombbal tudjuk legegyszerűbben kimásolni
- - - - - ![image](https://user-images.githubusercontent.com/13373740/165829067-d2bee694-6cb5-4959-bbc3-d99e4cae0883.png)
- Nyissuk meg a VS Code-ot
- Nyissunk új ablakot, ha nem üres az ablak (File/New Window)
- Kattintsunk a clone repository gombra (2 is van)
- - - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166056067-8cf3197f-47f0-4584-a9d2-360729305906.png)
- A felső sávban megjelenik egy clone from git parancs és felette a mezőben villog a kurzor.
- Ide másoljuk be a https linket, amit a gitről copy-ztunk ki
- - - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166058758-a46a7dc1-d127-4248-bb09-592c087654f7.png)
- Az enter megnyomására megjelenik egy mappa választó
- Itt válasszuk ki a mappát, ahol a gépen tárolni szeretnénk a dolgokat (magának a fájloknak létre fogja hozni a saját mappáját, ez látható a képen, hogy utána hogy néz ki)
- Én személy szerint a C:\repos mappát szoktam megadni ilyenkor, mert rövid az út oda (pl parancssorból fájl linkelésnél röviden megússzuk a linket)
- - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166064169-2453bfb0-5654-4965-ab3b-a1444bd08aa9.png)

## Új verzió letöltése
A git használatának a legnagyobb előnye, hogy írhatunk a jegyzetbe, mert amikor új verzió jön, a változásokat húzzuk csak le vele. Ha egy fájlon módosított a változás és te is, akkor conflict keletkezik. Ezeket kézzel fel tudjuk oldani, és a saját jegyzettel haladni tovább.
Az új verziót a következőképp tudjuk letölteni:
- Navigáljunk a Source Control (git) csempére a VS Code bal oldalán
- Itt látjuk a változtatásokat, a changes alatt
- - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166070834-ff065294-c85e-484f-86cf-a9eec6880e12.png)
- Első lépésben commitolni kell a változtatásainkat (Ez a parancs arra való, hogy egy csomagba pakoljuk a változtatásokat, így össze tudjuk hasonlítani a lehúzott verzióval)
- Ehhez ki kell valamit írni a message mezőbe, majd a pipára nyomni.
- Mivel nem szeretnénk a változtatásokat feltölteni a gitre, csak lehúzni az új dolgokat a gitről, nem számít, milyen üzenetet írunk ide esetünkben "a"
- - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166073643-0d0a512b-c175-4635-b334-1d3d6e8b0ffb.png)
- NE NYOMJUNK RÁ! Ekkor megjelenik egy kék gomb, ami arra való, hogy minden változtatást letöltsön, és/vagy feltöltsön a szerverre.
- Ehelyett a ...-nál nyomjunk a pull gombra. Ezzel csak a szerver változtatásait húzzuk le
- - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166074279-b3553cfd-c667-4dbd-9fdd-2a81b1ad5565.png)
- Így ha nem volt ütközés (konflict), már utána is van húzva a jegyzetünk.
- Ha volt valami, amit nem tudott feloldani a git, a változtatásoknál megjelenik a merge branch kiirat
- Itt egyessével végig lépkedve tudjuk nézni, hogy milyen változtatások voltak a saját gépen és a szerveren
- A fájlokban a kiválasztott verzió felett az Accept gomb megnyomásával tudjuk kiválasztani, melyik verzióval menjünk tovább. (Ha ilyennel találkozunk, érdemes végignézni compare changes nézetet, hogy pontosan mire jó)
- Ha mindent feloldottunk, a merge listán a + jellel tudjuk menteni a döntéseinket
- Ezt követően comittal tudjuk ellenőrizni, hogy minden rendben van-e
- - - - - - - ![image](https://user-images.githubusercontent.com/13373740/166075610-b78da85f-d964-4bac-bad8-6d9eb9b85bd0.png)
