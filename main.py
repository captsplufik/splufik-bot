import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === REPLACE WITH YOUR ACTUAL BOT TOKEN ===
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Presale constants
PRESALE_WALLET = "UQC6_hQoFH_S0zAnK2fFMuAxMIqgIssXjYuqtCJtKBKeN8sI"
SPK_PRICE = 0.05
SPK_LINK = "https://spk-presale.vercel.app"
WHITEPAPER_LINK = "https://spk-presale.vercel.app/whitepaper.html"
TELEGRAM_LINK = "https://t.me/+pfQZh-Qznfk4Yzdh"
TWITTER_LINK = "https://x.com/splufictoken"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🚀 *Welcome to the Splufik (SPK) Presale Bot!*

"
        "Use the buttons below to navigate:
"
    )
    keyboard = [
        [InlineKeyboardButton("💰 Buy SPK", callback_data='buy')],
        [InlineKeyboardButton("📜 Whitepaper", url=WHITEPAPER_LINK)],
        [InlineKeyboardButton("🪂 Airdrop Info", callback_data='airdrop')],
        [InlineKeyboardButton("📊 Presale Status", callback_data='status')],
        [InlineKeyboardButton("💬 Join Telegram", url=TELEGRAM_LINK)]
    ]
    await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💰 *Buy SPK Tokens*

Send TON to the wallet address below:

"
        f"`{PRESALE_WALLET}`

"
        f"🔹 Price: {SPK_PRICE} TON per SPK

After sending, you'll be eligible for airdrops if you meet the requirements.",
        parse_mode="Markdown"
    )

async def airdrop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🪂 *SPK Airdrop Eligibility*

"
        "To qualify:
"
        "1. Buy at least 5,000 SPK
"
        "2. Refer at least 3 users
"
        "3. Follow us on Twitter and Telegram

"
        f"🔗 [Presale Website]({SPK_LINK})
"
        f"🔗 [Twitter]({TWITTER_LINK})
"
        f"🔗 [Telegram]({TELEGRAM_LINK})",
        parse_mode="Markdown"
    )

async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔓 *Claim SPK Airdrop*

"
        "Auto-claim will be enabled after presale ends. Make sure you've:
"
        "✅ Bought ≥ 5,000 SPK
"
        "✅ Referred 3+ people
"
        "✅ Followed on socials

Stay tuned for claim updates!"
    )

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    referral_link = f"https://t.me/splufik_presale_bot?start={user_id}"
    await update.message.reply_text(
        f"📢 *Your SPK Referral Link:*

`{referral_link}`

"
        "Share this with others. When 3 users join through your link & meet airdrop conditions, you qualify!",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 *Presale Status*

"
        "🔥 Total Raised: 20,000 TON
"
        "🎯 Target: 5,000,000 TON
"
        "⏳ Ends: June 16, 2026

"
        f"View live stats at: {SPK_LINK}",
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("airdrop", airdrop))
app.add_handler(CommandHandler("claim", claim))
app.add_handler(CommandHandler("referral", referral))
app.add_handler(CommandHandler("status", status))

app.run_polling()
