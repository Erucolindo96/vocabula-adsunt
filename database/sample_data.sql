
DELETE FROM book;
DELETE FROM age;


INSERT INTO age VALUES
(0, 'Romantyzm', 'romantyzm'),
(1, 'Średniowiecze', 'sredniowiecze');

INSERT INTO book VALUES
(0, 'Pan Tadeusz księga 13', 'Pan Tadeusz i Zosia', 'api/ksiega-trzynasta', 0, 'Adam Mickiewicz', 'adam-mickiewicz'),
(1, 'Disy na Mickiewicza', 'Mówisz Adamie, ześ jest narodu wieszczem a tak naprawdę jesteś zwykłym leszczem',
null,0, 'Juliusz Słowacki', 'juliusz-slowacki'),
(2, 'Gaude Mater Polonia', null, 'api/gaude-mater-polonia',1, 'Władysław z Gielniowa', 'wladyslaw-z-gielniowa'),
(3, 'Bajka o Romantyzmie', 'Roman Tyźmie dziecko zrobił', 'www.wiocha.pl',0, null, null),
(4, 'Gall Anonim', null, null, null, null, null);