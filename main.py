# ============================================================
# TELEGRAM DASTURLASH TILLARI BOTI
# Fayl nomi: main.py
# ============================================================

import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)


# ============================================================
# TOKEN
# BOTFATHER BERGAN YANGI TOKENNI SHU YERGA YOZASIZ
# Tokenni hech kimga yubormang!
# ============================================================

TOKEN = "8992551057:AAEWiuhS9KqBcO5ly_J0YGc21djq2fFSAaE"


# ============================================================
# MAJBURIY KANAL
#
# Siz bergan:
# https://t.me/vnshablonlar001orifjon
#
# Shuning uchun username:
# @vnshablonlar001orifjon
#
# AGAR SIZNING HAQIQIY KANALINGIZ @Uzbs.gr BO'LSA,
# PASTDAGI IKKALA QATORNI HAM O'Z KANALINGIZGA MOSLANG.
# ============================================================

CHANNEL_USERNAME = "@vnshablonlar001orifjon"

CHANNEL_LINK = "https://t.me/vnshablonlar001orifjon"


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ============================================================
# DASTURLASH TILLARI MA'LUMOTLARI
# ============================================================

LANGUAGES = {

    "python": """🐍 PYTHON

📅 Yaratilgan yili: 1991-yil.
👨‍💻 Yaratuvchisi: Guido van Rossum.
🌍 Kelib chiqishi: Niderlandiya.
🎯 Python dasturlarni sodda va tushunarli yozish uchun yaratilgan.
⚡ Bu yuqori darajadagi, umumiy maqsadli dasturlash tilidir.
🌐 Web, sun'iy intellekt, Data Science va avtomatlashtirishda ishlatiladi.
📚 Django, Flask va FastAPI kabi frameworklari mavjud.
🚀 Python bugungi kunda eng mashhur dasturlash tillaridan biridir.""",

    "javascript": """🟨 JAVASCRIPT

📅 Yaratilgan yili: 1995-yil.
👨‍💻 Yaratuvchisi: Brendan Eich.
🏢 Dastlab Netscape kompaniyasida ishlab chiqilgan.
🎯 Web-sahifalarni interaktiv qilish uchun yaratilgan.
🌐 Hozir Frontend va Backend dasturlashda ishlatiladi.
⚙️ Node.js orqali server dasturlari ham yoziladi.
📱 Web-ilovalar yaratishda juda keng qo'llanadi.
🚀 React, Vue va Angular JavaScript ekotizimida mashhur.""",

    "js": """🟨 JAVASCRIPT

📅 Yaratilgan yili: 1995-yil.
👨‍💻 Yaratuvchisi: Brendan Eich.
🏢 Netscape kompaniyasida ishlab chiqilgan.
🎯 Web-sahifalarga interaktivlik berish uchun yaratilgan.
🌐 Frontend va Backend dasturlashda ishlatiladi.
⚙️ Node.js orqali server dasturlari yaratiladi.
📱 Web-ilovalar yaratishda keng qo'llanadi.
🚀 JavaScript zamonaviy Web dasturlashning asosiy texnologiyalaridan biridir.""",

    "html": """🌐 HTML

📅 Yaratilgan yili: 1991-yil.
👨‍💻 Asosiy yaratuvchisi: Tim Berners-Lee.
🌍 World Wide Web loyihasi va CERN bilan bog'liq.
🎯 Web-sahifaning tuzilishini yaratish uchun ishlatiladi.
🧱 HTML dasturlash tili emas, markup belgilash tilidir.
📄 Matn, rasm, havola, jadval va boshqa elementlarni joylashtiradi.
🎨 HTML odatda CSS bilan birga ishlatiladi.
⚡ JavaScript esa HTML sahifalariga interaktivlik qo'shadi.""",

    "css": """🎨 CSS

📅 CSS 1990-yillarda ishlab chiqilgan.
👨‍💻 Asosiy yaratuvchisi: Håkon Wium Lie.
🌍 Web standartlari rivojlanishi bilan W3C tomonidan standartlashtirilgan.
🎯 Web-sahifalarning tashqi ko'rinishini boshqarish uchun yaratilgan.
🎨 Rang, shrift, o'lcham va joylashuvni belgilaydi.
📐 Flexbox va Grid zamonaviy CSS imkoniyatlaridir.
📱 Responsive dizayn yaratishda juda muhim.
💡 HTML tuzilmani, CSS esa dizaynni boshqaradi.""",

    "c++": """⚙️ C++

📅 Ishlab chiqilishi 1979-yilda boshlangan.
👨‍💻 Yaratuvchisi: Bjarne Stroustrup.
🌍 Bell Labs, AQShda ishlab chiqilgan.
🎯 C tilini obyektga yo'naltirilgan imkoniyatlar bilan kengaytirish maqsad qilingan.
⚡ Juda tez ishlaydigan dasturlar yaratish imkonini beradi.
🎮 O'yinlar va game engine'larda keng ishlatiladi.
🖥️ Operatsion tizimlar va tizimli dasturlarda ham ishlatiladi.
🚀 C++ professional dasturlashda muhim tillardan biridir.""",

    "c": """🔵 C

📅 Yaratilgan yili: 1970-yillar boshida.
👨‍💻 Asosiy yaratuvchisi: Dennis Ritchie.
🌍 Bell Labs, AQShda ishlab chiqilgan.
🎯 Operatsion tizimlar va tizimli dasturlar yaratish uchun rivojlantirilgan.
⚡ Tezkor va resurslardan samarali foydalanadi.
🖥️ Unix operatsion tizimining rivojlanishida katta rol o'ynagan.
🔧 Embedded systems va mikrokontrollerlarda ishlatiladi.
🏆 Ko'plab zamonaviy tillarga katta ta'sir ko'rsatgan.""",

    "java": """☕ JAVA

📅 Ishlab chiqilishi 1990-yillarning boshida boshlangan.
👨‍💻 Asosiy yaratuvchisi: James Gosling.
🏢 Sun Microsystems kompaniyasida ishlab chiqilgan.
🌍 AQSh bilan bog'liq texnologiya.
🎯 Turli platformalarda ishlaydigan dasturlar yaratish maqsad qilingan.
🖥️ Java dasturlari JVM orqali ishlaydi.
🌐 Serverlar, korporativ tizimlar va Android'da keng qo'llangan.
🚀 Java yirik dasturiy loyihalarda hanuz keng ishlatiladi.""",

    "php": """🐘 PHP

📅 Yaratilgan yili: 1994-yil.
👨‍💻 Yaratuvchisi: Rasmus Lerdorf.
🌍 Dastlab Web dasturlash uchun ishlab chiqilgan.
🎯 Dinamik Web-sahifalar yaratish uchun yaratilgan.
🌐 Asosan server tomonida ishlaydi.
🗄️ MySQL va boshqa ma'lumotlar bazalari bilan ishlaydi.
🖥️ WordPress PHP texnologiyasidan foydalanadi.
🚀 Laravel va Symfony kabi frameworklari mavjud.""",

    "c#": """🟣 C#

📅 Ishlab chiqilishi 1999-yilda boshlangan.
👨‍💻 Anders Hejlsberg boshchiligidagi Microsoft jamoasi yaratgan.
🏢 Microsoft tomonidan ishlab chiqilgan.
🌍 AQShdagi Microsoft kompaniyasi bilan bog'liq.
🎯 .NET platformasi uchun zamonaviy dasturlash tili sifatida yaratilgan.
🖥️ Desktop, Web va Cloud dasturlarida ishlatiladi.
🎮 Unity orqali o'yin yaratishda juda mashhur.
🚀 C# .NET ekotizimining asosiy tillaridan biridir.""",

    "ruby": """💎 RUBY

📅 1990-yillarda yaratilgan.
👨‍💻 Yaratuvchisi: Yukihiro Matsumoto.
🌍 Yaponiya.
🎯 Dasturchilar uchun qulay va o'qilishi oson til yaratish maqsad qilingan.
💎 Ruby obyektga yo'naltirilgan dasturlashni qo'llab-quvvatlaydi.
🌐 Ruby on Rails Web dasturlashda mashhur.
🖥️ Web-ilovalar va server dasturlarida ishlatiladi.
🚀 Ruby soddaligi bilan tanilgan.""",

    "go": """🐹 GO

📅 2007-yilda Google'da ishlab chiqila boshlangan.
👨‍💻 Robert Griesemer, Rob Pike va Ken Thompson yaratgan.
🏢 Google tomonidan ishlab chiqilgan.
🎯 Tezkor va katta server tizimlarini yaratishni osonlashtirish maqsad qilingan.
⚡ Go kompilyatsiya qilinadigan tezkor tildir.
🌐 Backend va Cloud dasturlashda ishlatiladi.
🔄 Goroutine parallel ishlashni qulaylashtiradi.
🚀 Docker va Kubernetes ekotizimida Go muhim rol o'ynaydi.""",

    "swift": """🍎 SWIFT

📅 2014-yilda taqdim etilgan.
👨‍💻 Apple kompaniyasi jamoasi tomonidan ishlab chiqilgan.
🏢 Apple tomonidan yaratilgan.
🌍 AQSh.
🎯 Apple qurilmalari uchun zamonaviy dasturlar yaratish maqsad qilingan.
📱 iPhone va iPad dasturlarida keng ishlatiladi.
💻 macOS, watchOS va tvOS uchun ham ishlatiladi.
🚀 Apple ekotizimidagi asosiy dasturlash tillaridan biridir.""",

    "kotlin": """🟠 KOTLIN

📅 2011-yilda taqdim etilgan.
👨‍💻 JetBrains kompaniyasi tomonidan ishlab chiqilgan.
🌍 JetBrains kompaniyasi Chexiya bilan bog'liq.
🎯 Java bilan birga ishlay oladigan zamonaviy til yaratish maqsad qilingan.
📱 Android dasturlashda juda keng ishlatiladi.
☕ Java kodlari bilan birgalikda ishlay oladi.
🛡️ Null safety kabi imkoniyatlarga ega.
🚀 Android uchun eng muhim zamonaviy tillardan biridir.""",

    "typescript": """🔷 TYPESCRIPT

📅 2012-yilda taqdim etilgan.
👨‍💻 Microsoft jamoasi tomonidan ishlab chiqilgan.
🌍 Microsoft, AQSh.
🎯 JavaScript'ga statik tiplash imkoniyatlarini qo'shish uchun yaratilgan.
🧩 TypeScript JavaScript kodiga kompilyatsiya qilinadi.
🌐 Katta Web loyihalarida juda foydali.
⚛️ React, Angular va boshqa texnologiyalar bilan ishlatiladi.
🚀 Zamonaviy Frontend dasturlashda juda mashhur.""",
}


# ============================================================
# TURFA NOMLARNI BIR NOMGA O'GIRISH
# ============================================================

ALIASES = {
    "python": "python",
    "питон": "python",
    "пайтон": "python",

    "javascript": "javascript",
    "java script": "javascript",
    "js": "js",

    "html": "html",
    "html5": "html",

    "css": "css",
    "css3": "css",

    "c++": "c++",
    "cpp": "c++",

    "c": "c",

    "java": "java",

    "php": "php",

    "c#": "c#",
    "csharp": "c#",
    "c sharp": "c#",

    "ruby": "ruby",

    "go": "go",
    "golang": "go",

    "swift": "swift",

    "kotlin": "kotlin",

    "typescript": "typescript",
    "type script": "typescript",
    "ts": "typescript",
}


# ============================================================
# KANAL A'ZOLIGINI TEKSHIRISH
# ============================================================

async def check_member(user_id, bot):

    try:

        member = await bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=user_id
        )

        # Kanalga a'zo, administrator yoki creator bo'lsa
        if member.status in ("member", "administrator", "creator"):
            return True

        # Ba'zi hollarda foydalanuvchi kanalni tark etgan bo'lishi mumkin
        return False

    except Exception as error:

        logger.error(
            f"Kanal a'zoligini tekshirishda xato: {error}"
        )

        return False


# ============================================================
# KANALGA OBUNA BO'LISH TUGMALARI
# ============================================================

def subscription_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📢 Kanalga qo'shilish",
                url=CHANNEL_LINK
            )
        ],
        [
            InlineKeyboardButton(
                "✅ Tekshirish",
                callback_data="check_subscription"
            )
        ]
    ])


# ============================================================
# /START
# ============================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.effective_user or not update.message:
        return

    user_id = update.effective_user.id

    is_member = await check_member(
        user_id,
        context.bot
    )

    if is_member:

        await update.message.reply_text(
            "🎉 Xush kelibsiz!\n\n"
            "✅ Siz kanalga a'zosiz.\n\n"
            "👨‍💻 Endi menga dasturlash tili yoki "
            "texnologiya nomini yuboring.\n\n"
            "Masalan:\n"
            "🐍 Python\n"
            "🌐 HTML\n"
            "🎨 CSS\n"
            "🟨 JavaScript\n"
            "⚙️ C++\n"
            "☕ Java\n"
            "🐘 PHP\n"
            "🟣 C#"
        )

    else:

        await update.message.reply_text(
            "🔒 Botdan foydalanish uchun avval "
            "quyidagi kanalga obuna bo'ling.\n\n"
            "1️⃣ «📢 Kanalga qo'shilish» tugmasini bosing.\n"
            "2️⃣ Kanalga a'zo bo'ling.\n"
            "3️⃣ «✅ Tekshirish» tugmasini bosing.",
            reply_markup=subscription_keyboard()
        )


# ============================================================
# TEKSHIRISH TUGMASI
# ============================================================

async def check_button(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    if query is None:
        return

    user_id = query.from_user.id

    try:

        is_member = await check_member(
            user_id,
            context.bot
        )

        if is_member:

            # MUHIM:
            # query.answer() faqat bir marta chaqiriladi
            await query.answer(
                "✅ A'zolik tasdiqlandi!"
            )

            await query.message.edit_text(
                "🎉 Tabriklayman!\n\n"
                "✅ Siz kanalga a'zo bo'ldingiz!\n\n"
                "👨‍💻 Endi dasturlash tili yoki "
                "texnologiya nomini yuboring.\n\n"
                "Masalan: Python"
            )

        else:

            await query.answer(
                "❌ Siz hali kanalga a'zo emassiz!",
                show_alert=True
            )

    except Exception as error:

        logger.exception(
            "TEKSHIRISHDA XATO"
        )

        try:
            await query.answer(
                "⚠️ Tekshirishda xatolik yuz berdi.",
                show_alert=True
            )
        except Exception:
            pass


# ============================================================
# DASTURLASH TILI HAQIDA MA'LUMOT
# ============================================================

async def language_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.effective_user or not update.message:
        return

    user_id = update.effective_user.id

    # Har bir so'rovda yana kanalni tekshiramiz
    is_member = await check_member(
        user_id,
        context.bot
    )

    if not is_member:

        await update.message.reply_text(
            "🔒 Avval kanalga a'zo bo'ling.",
            reply_markup=subscription_keyboard()
        )

        return

    text = update.message.text.strip().lower()

    # Keraksiz belgilarni biroz tozalaymiz
    text = text.replace("ё", "е")

    language_key = ALIASES.get(text)

    if language_key:

        information = LANGUAGES[language_key]

        await update.message.reply_text(
            information
        )

        return

    await update.message.reply_text(
        "❓ Bu til yoki texnologiya ma'lumotlar bazasida topilmadi.\n\n"
        "📚 Quyidagilardan birini yuboring:\n\n"
        "🐍 Python\n"
        "🟨 JavaScript\n"
        "🌐 HTML\n"
        "🎨 CSS\n"
        "⚙️ C++\n"
        "🔵 C\n"
        "☕ Java\n"
        "🐘 PHP\n"
        "🟣 C#\n"
        "💎 Ruby\n"
        "🐹 Go\n"
        "🍎 Swift\n"
        "🟠 Kotlin\n"
        "🔷 TypeScript"
    )


# ============================================================
# BOTDAGI XATOLARNI KO'RSATISH
# ============================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    logger.error(
        "BOTDA XATOLIK:",
        exc_info=context.error
    )


# ============================================================
# BOTNI ISHGA TUSHIRISH
# ============================================================

def main():

    if (
        not TOKEN
        or TOKEN == "BU_YERGA_YANGI_BOT_TOKENINGIZNI_QOYING"
    ):

        print()
        print("❌ TOKEN KIRITILMAGAN!")
        print()
        print(
            "main.py faylidagi TOKEN qatoriga "
            "BotFather bergan yangi tokenni yozing."
        )
        print()

        return

    application = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    # /start komandasi
    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # Tekshirish tugmasi
    application.add_handler(
        CallbackQueryHandler(
            check_button,
            pattern="^check_subscription$"
        )
    )

    # Foydalanuvchi yuborgan oddiy matn
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            language_info
        )
    )

    # Xatolar
    application.add_error_handler(
        error_handler
    )

    print()
    print("======================================")
    print("🤖 TELEGRAM BOT ISHGA TUSHDI!")
    print("📡 Bot Telegram serverini kutmoqda...")
    print("✅ /start ishlaydi")
    print("✅ Kanal tekshirish ishlaydi")
    print("✅ Dasturlash tillari ishlaydi")
    print("======================================")
    print()

    # Botni ishga tushirish
    application.run_polling(
        drop_pending_updates=True
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    main()