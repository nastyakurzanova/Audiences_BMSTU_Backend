import random

from django.core.management.base import BaseCommand
from booking.models import *
from .utils import random_date, random_timedelta


def add_pioneers():
    Audiences.objects.create(
        name="Христофор Колумб",
        date_birthday=1451,
        date_death=1506,
        description="""Христофо́р Колу́мб (итал. Cristoforo Colombo, исп. Cristóbal Colón, лат. Christophorus Columbus; между 26 августа и 31 октября 1451, Генуэзская республика — 20 мая 1506, Вальядолид, Королевство Кастилия и Леон) — испанский мореплаватель итальянского происхождения, в 1492 году открывший для европейцев Новый Свет (Америку).

Колумб первым из достоверно известных путешественников пересёк Атлантический океан в субтропической и тропической полосе Северного полушария и первым из европейцев ходил в Карибском море и в Саргассовом море[3]. Он открыл Южную Америку и Центральную Америку и положил начало их исследованию, включая континентальные части и близлежащие архипелаги — Большие Антильские (Куба, Гаити, Ямайка и Пуэрто-Рико), Малые Антильские (от Доминики до Виргинских островов, а также Тринидад) и Багамские острова.

Первооткрывателем Америки для европейцев Колумба можно назвать с оговорками, ведь ещё в Средние века на территории Северной Америки бывали европейцы в лице исландских викингов (см. Винланд). Но поскольку за пределами Скандинавии сведений об этих походах не было, именно экспедиции Колумба впервые сделали сведения о землях на западе всеобщим достоянием и положили начало колонизации Америки европейцами.

Всего Колумб совершил 4 плавания к берегам Америки"""
    )

    Audiences.objects.create(
        name="Кук Фредерик",
        date_birthday=1865,
        date_death=1940,
        description="Фредерик Кук родился в семье немецких иммигрантов; несмотря на неблагоприятные жизненные обстоятельства и бедность, получил медицинское образование. Впервые участвовал в арктической экспедиции в 1891—1892 годах в составе отряда Пири в Северной Гренландии; в 1893—1894 годах в летний сезон предпринял два самостоятельных плавания к побережью Гренландии. В 1897—1898 годах участвовал в Бельгийской антарктической экспедиции, совершившей незапланированный дрейф в Море Беллинсгаузена. Во время путешествия познакомился с Руалем Амундсеном, штурманом экспедиции, и до самой его гибели в 1928 году исследователи поддерживали дружеские отношения. В 1894—1913 годах Фредерик Кук состоял действительным членом Арктического клуба, является одним из его основателей. В 1900 году Кук в очередной раз посетил Гренландию, где Роберт Пири находился в экспедиции, и отказался остаться с ним на зимовку. В 1903—1906 годах Кук занимался исследованиями на Аляске и предпринял попытку покорения вершины Мак-Кинли. В 1904 году стал одним из сооснователей Клуба Исследователей[en], в 1907—1908 годах был избран его почётным президентом. В 1907—1909 годах вновь находился в Арктике, объявив о попытке достижения Северного полюса. После неудачных судебных разбирательств с Пири, в 1910—1916 годах проводил многочисленные лекционные турне, распространяя книги о путешествии в Центральную Арктику; совершил кругосветное путешествие. После завершения карьеры путешественника занимался разведкой и продажей нефтеносных земель на Западе США. По обвинению в мошенничестве был осуждён на длительное тюремное заключение, которое отбывал в 1924—1930 годах. После освобождения за отсутствием состава преступления (все проданные участки были прибыльными) работал врачом и пытался восстановить репутацию и свой приоритет. Незадолго до кончины в 1940 году указом президента США Ф. Рузвельта был реабилитирован по всем пунктам обвинения. С 1956 года функционирует Общество Фредерика Кука, которое исследует его наследие и добивается признания приоритета в географических открытиях."
    )

    Audiences.objects.create(
        name="Михаил Петрович Лазарев",
        date_birthday=1788,
        date_death=1851,
        description="""Родился в губернском городе Владимире. Сын сенатора Петра Гавриловича Лазарева, происходившего из дворян Арзамасского уезда Нижегородской губернии. Незадолго до смерти, в 1800 году отец определил троих сыновей — Андрея, Михаила, Алексея — в Морской кадетский корпус. При этом попечение над осиротевшими братьями взял на себя друг их отца — поэт Гавриил Романович Державин, не имевший своих детей.

В 1803 году выдержал экзамен на звание гардемарина, став третьим по успеваемости из 32 учеников. В числе 30 лучших выпускников корпуса отправлен в Великобританию, где служил военным на флоте до 1808 года для ознакомления с постановкой военно-морского дела в иностранных портах. В течение пяти лет находился в непрерывном плавании в Атлантическом океане и Средиземном море.

Произведён в мичманы 21 мая 1808 года как «прибывший из Англии».

В 1808—1813 годах служил на Балтийском флоте. Участвовал в Русско-шведской 1808—1809 годов и Отечественной войне 1812 года.

Совместно с Фаддеем Беллинсгаузеном командовал Первой русской антарктической экспедицией 1819—1821 годов, которая впервые в истории человечества подошла к шельфовым ледникам Антарктиды.
        """
    )

    Audiences.objects.create(
        name="Фернан Магеллан",
        date_birthday=1480,
        date_death=1521,
        description="Ферна́н Магелла́н (Ферна́у ди Магалья́йнш[2][3], порт. Fernão de Magalhães [fɨɾˈnɐ̃w̃ ðɨ mɐɡɐˈʎɐ̃ȷ̃s]; Ферна́ндо (Эрна́ндо) де Магалья́нес, исп. Fernando (Hernando) de Magallanes [(f)eɾ'nando ðe maɣa'ʎanes]; лат. Ferdinandus Magellanus; 20 ноября 1480 — 27 апреля 1521) — португальский и испанский[4] мореплаватель с титулом аделантадо. Командовал экспедицией, совершившей первое из известных кругосветных путешествий. Открыл пролив, позже названный его именем, став первым европейцем, проследовавшим по морю из Атлантического океана в Тихий. Погиб во время путешествия, не успев лично завершить его."
    )

    Audiences.objects.create(
        name="А́льваро Менда́нья де Не́йра",
        date_birthday=1541,
        date_death=1595,
        description="""
Родился в Сарагосе в дворянской семье. В 1558 году прибыл в Перу по приглашению своего дяди колониального чиновника Лопе Гарсия де Кастро[2], где занимал различные административные должности. В 1567 году поставлен был своим дядей, незадолго до этого ставшим вице-королём Перу, во главе экспедиции для исследования и покорения Неведомых Южных Земель[3].

Два корабля Менданьи, 250-тонный «Лос Рейес» и 110-тонный «Тодос Сантос»[4], на которых находилось 125 солдат и матросов, отплыли из Кальяо 19 ноября 1567 года[5], и, после длительного путешествия, 7 февраля 1568 года открыли Соломоновы острова и исследовали основные из них. Никакого золота на архипелаге найдено не было, а подавляющее большинство местных племён встретило испанцев недружелюбно. Экспедиция также открыла архипелаг Тувалу и атолл Уэйк.

По возвращении в Перу, в 1569 году, Менданья опубликовал отчет о своих открытиях, в котором описывал Соломоновы острова как «очень богатую страну». Однако, из-за войн, которые вела в то время Испания, он не смог получить средства, необходимые для второй экспедиции. Только в 1594 году испанский король Филипп II приказал основать колонию на Соломоновых островах и назначил Менданью губернатором Сан-Кристобаля.

11 апреля 1595 года, снарядив четыре судна, «Сан-Херонимо», «Санта-Исабель», «Сан-Фелипе» и «Санта-Каталина»[6], на которых находилось всего 378 человек, 280 из которых являлись солдатами[7], Менданья, получивший незадолго до этого титул аделантадо, отплыл из Кальяо. Главным навигатором экспедиции был Педро де Кирос, а самого Менданью сопровождала супруга Изабелла де Баррето. 21 июля Менданья достиг группы островов, которые он назвал островами Маркиза де Мендоса (Маркизскими), в честь супруги тогдашнего вице-короля Перу Гарсиа де Мендосы, маркиза Каньете[2]. Продолжая плавание к Соломоновым островам, экспедиция обнаружила большой остров Санта-Крус, на котором и была основана испанская колония[8].
"""
    )

    Audiences.objects.create(
        name="Америго Веспуччи",
        date_birthday=1454,
        date_death=1512,
        description="""
        Аме́риго Веспу́ччи (итал. Amerigo Vespucci, лат. Americus Vespucius; 9 марта 1454, Флоренция, Флорентийская республика — 22 февраля 1512, Севилья, Испания) — флорентийский путешественник и мореплаватель, в честь которого была названа Америка.

Отправившись в 1501—1502 годах в плавание к берегам Бразилии и Вест-Индии, доказал, что данные территории являются не восточной окраиной Азии (как первоначально предполагалось из путешествий Колумба), а отдельным континентом, описанным как «Новый Свет». В 1507 году новый континент был назван Америкой в честь латинской версии имени Веспуччи[2].
"""
    )

    print("Услуги добавлены")


def add_discoveries():
    users = CustomUser.objects.filter(is_moderator=False)
    moderators = CustomUser.objects.filter(is_moderator=True)
    
    if len(users) == 0:
        print("Заявки не могут быть добавлены. Сначала добавьте пользователей с помощью команды add_users")
        return

    pioneers = Audiences.objects.all()

    for _ in range(10):
        discovery = Booking.objects.create()
        discovery.name = "Открытие №" + str(discovery.pk)
        discovery.status = random.randint(2, 5)

        if discovery.status in [3, 4]:
            discovery.date_complete = random_date()
            discovery.date_of_formation = discovery.date_complete - random_timedelta()
            discovery.date_created = discovery.date_of_formation - random_timedelta()
            discovery.moderator = random.choice(moderators)
        else:
            discovery.date_of_formation = random_date()
            discovery.date_created = discovery.date_of_formation - random_timedelta()

        discovery.user = random.choice(users)

        for i in range(random.randint(1, 5)):
            discovery.pioneers.add(random.choice(pioneers))

        discovery.save()

    print("Заявки добавлены")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # management.call_command("clean_db")

        add_pioneers()
        add_discoveries()










