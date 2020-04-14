
DELETE FROM book;
DELETE FROM author;
DELETE FROM age;


INSERT INTO author VALUES
(0, 'Adam Mickiewicz'),
(1, 'Juliusz Słowacki co kocha wacki'),
(2, 'Władysław z Gielniowa');

INSERT INTO age VALUES
(0, 'Romantyzm'),
(1, 'Średniowiecze');

INSERT INTO book VALUES
(0, 'Pan Tadeusz księga 13', 'Pan Tadeusz i Zosia', 'api/ksiega-trzynasta', 0, 0),
(1, 'Disy na Mickiewicza', 'Mówisz Adamie, ześ jest narodu wieszczem a tak naprawdę jesteś zwykłym leszczem',
null, 1, 0),
(2, 'Gaude Mater Polonia', null, 'api/gaude-mater-polonia', 2, 1),
(3, 'Bajka o Romantyzmie', 'Roman Tyźmie dziecko zrobił', 'www.wiocha.pl', null, 0),
(4, 'Gall Anonim', null, null, null, null);