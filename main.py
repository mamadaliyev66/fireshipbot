from aiogram import Dispatcher , Bot,executor,types
from aiogram.types import reply_keyboard,ReplyKeyboardMarkup
from base import part_1,part_2,basic_concepts,advanced_concepts,algorithms,dream_app,animal_farm
from base import advanced_techniques,example_models,bonus,intro,core_concepts,relational_data_modeling
bot_token="5893385203:AAFTHHabQx_8Dpg8Q3tELFTcsUxXlRRGCiA"

bot=Bot(token=bot_token)
dp=Dispatcher(bot)

try:
    menus=[
        ["Modern Java Script"],
        ["React - The Full Course"],
        ["Firestore Data Modelling"]
    ]

    reply_menu=ReplyKeyboardMarkup(keyboard=menus,resize_keyboard=True)
    @dp.message_handler(commands=['Start','start'])
    async def Start(message:types.Message):
        await message.answer(
            f"Well Come to 🔥Fireship Bot !\nYou Can Watch and Download All 🔥Fireship Videos from Here !\nIt's Free Enjoy 😉",
            reply_markup=reply_menu
        )
        await bot.send_message(chat_id=1234715065,text=f"You Have a New User : {message.from_user.full_name} , {message.from_user.username} ,{message.from_user.id}")

    ## JS videos

    js_rp_menus=[
        ["1.Basic Concepts"],
        ["2.Advanced Concepts"],
        ["3.Algorithms"],
        ["4.Dream App"],
        ["🔙Back"]
    ]

    js_menus=ReplyKeyboardMarkup(keyboard=js_rp_menus,resize_keyboard=True)


    react_rp_keyboard=[
        ["Part 1"],
        ["Part 2"],
        ["Animal Farm"],
        ["🔙Back"]
    ]

    firebase_dm=[
        ['1.Intro'],
        ["2.Core Concepts"],
        ["3.Relational Data Modeling"],
        ["4.Advanced Techniques"],
        ["5.Example Models"],
        ["6.Bonus Round"],
        ["🔙Back"]
    ]

    firebase_keyboard=ReplyKeyboardMarkup(keyboard=firebase_dm,resize_keyboard=True)


    react_keyboard=ReplyKeyboardMarkup(keyboard=react_rp_keyboard,resize_keyboard=True)
    @dp.message_handler()
    async def JavaScript(message:types.Message):
        global basic_concepts
        text=message.text
        if text=='Modern Java Script':
            await message.answer(
            f"Modern JavaScript Full Course\n\n"
                f"What will I learn?\n\n"
                f"This course is focusd on the basics of JavaScript - the world’s most commonly used programming language. Here’s what you’ll get out of it…\n\n👶 The Basics of JavaScript\n\n👨‍🎤 Advanced concepts broken down in a quick no-BS format\n\n📰 Prepare for JS interviews by coding algorithms\n\n🧪 Test Driven Development with Vitest\n\n⚔️ Debugging and Error Handling\n\n🎨 Build a text-to-image API with Node.js and OpenAI\n\n🗯️ Learn modern browser APIs like Fetch\n\n🍕 A great primer for more advanced Fireship courses",
                reply_markup=js_menus

            )
        if text=='1.Basic Concepts':
            for i in range(1,4):
                await bot.send_video(chat_id=message.from_user.id,video=basic_concepts[i]['id'],caption=basic_concepts[i]['name'])

        if text=="2.Advanced Concepts":
            for i in range(1, 10):
                await bot.send_video(chat_id=message.from_user.id, video=advanced_concepts[i]['id'],
                                    caption=advanced_concepts[i]['name'])
        if text=="3.Algorithms":
            for i in range(1, 5):
                await bot.send_video(chat_id=message.from_user.id, video=algorithms[i]['id'],
                                    caption=algorithms[i]['name'])
        if text=="4.Dream App":
            for i in range(1, 5):
                await bot.send_video(chat_id=message.from_user.id, video=dream_app[i]['id'],
                                    caption=dream_app[i]['name'])
        if text=="🔙Back":
            await message.answer(
                "Main Menu ",
                reply_markup=reply_menu
            )

        ########react js
        if text=='React - The Full Course':
            await bot.send_video(chat_id=message.from_user.id, video="BAACAgIAAx0CdCu1oAADUGQiu2Q1hKZhisCffoKbwX-Fl6IVAAL6LAAC-K4YSf9iBPhx3LiWLwQ",
                                caption=(f"React - The full course\n\n"
                f"Learn the fundamentals of React.js by building five apps from scratch.\n\n"
                f"React - The Full Course is unlike any other React course on the Internet. It provides a fast-paced introduction to essential concepts, then puts them into practice by building multiple fun and challenging full-stack apps from scratch.\n\n"
                f"What will I learn?\n\n"
                f"👨‍🎤 Everything you need to be productive with React\n\n"
                f"⚡ Breakdown of key concepts in 100 Seconds\n\n"
                f"📚 Design patterns and best practices\n\n"
                f"🎣 Component composition and custom hooks\n\n"
                f"🚀 Lazy loading with Suspense\n\n"
                f"📱 How to build Progressive Web Apps (PWAs)\n\n"
                f"🎨 Animation with Framer Motion\n\n"
                f"🐕 Advanced data fetching with SWR and React Query\n\n"
                f"⚛️ Complex dynamic forms with React Final Form\n\n"
                f"🔥 Manage realtime data with Firestore\n\n"
                f"📰 SSR with Next.js\n\n"
                f"🍰 More!\n\n"),reply_markup=react_keyboard
                                )

        if text =="Part 1":
            for i in range(1,9):
                await bot.send_video(chat_id=message.from_user.id, video=part_1[i]['id'],
                                    caption=part_1[i]['name'])
        if text =="Part 2":
            for i in range(1,9):
                await bot.send_video(chat_id=message.from_user.id, video=part_2[i]['id'],
                                        caption=part_2[i]['name'])
        if text =="Animal Farm":
            for i in range(1,4):
                await bot.send_video(chat_id=message.from_user.id, video=animal_farm[i]['id'],
                                    caption=animal_farm[i]['name'])


        if text=="Firestore Data Modelling":
            await bot.send_video(chat_id=message.from_user.id, video="BAACAgIAAx0CdCu1oAADuGQj5edfnGag-qx07znP4NX662baAAKoJgAC4dcgSc6HIlcaNuQKLwQ",
                                 caption="Firestore Data Modeling\n\n"
                                        "Tech Stacks\n\n"
                                        "Firebase + JavaScript\n\n"
                                        "The Firestore Data Modeling Course provides a foundation for modeling data relationships in NoSQL, while optimizing queries for performance, cost, and complexity. Determining the the optimal data model in Cloud Firestore is not an easy task because you need to anticipate your app’s UI/UX requirements in advance. Failure to consider the tradeoffs between various data models could lead to poor app performance and/or unnecessary cloud computing expenses. The goal of this course is to teach you the concepts necessary to make good decisions related to data modeling that minimize costs and maximize read performance.\n"
                                        "Topics Covered\n\n"
                                        "Core Concepts in Firestore.\n\n"
                                        "Comparisons to SQL data modeling.\n\n"
                                        "Advanced methods for reading and querying data.\n\n"
                                        "Relational data modeling concepts like one-to-one, one-to-many, and many-to-many.\n\n"
                                        "How to avoid common pitfalls and anti-patterns.\n\n"
                                        "Examples of data models for common real-world app features.\n\n",reply_markup=firebase_keyboard)
        if text=="1.Intro":
            for i in range(1,4):
                await bot.send_video(chat_id=message.from_user.id, video=intro[i]['id'],
                                    caption=intro[i]['name'])
        if text == "2.Core Concepts":
            for i in range(1, 7):
                await bot.send_video(chat_id=message.from_user.id, video=core_concepts[i]['id'],
                                     caption=core_concepts[i]['name'])
        if text == "3.Relational Data Modeling":
                for i in range(1, 5):
                    await bot.send_video(chat_id=message.from_user.id, video=relational_data_modeling[i]['id'],
                                         caption=relational_data_modeling[i]['name'])

        if text == "4.Advanced Techniques":
            for i in range(1, 3):
                await bot.send_video(chat_id=message.from_user.id, video=advanced_techniques[i]['id'],
                                     caption=advanced_techniques[i]['name'])
        if text == "5.Example Models":
            for i in range(1, 6):
                await bot.send_video(chat_id=message.from_user.id, video=example_models[i]['id'],
                                     caption=example_models[i]['name'])
        if text == "6.Bonus Round":
            for i in range(1, 3):
                await bot.send_video(chat_id=message.from_user.id, video=bonus[i]['id'],
                                     caption=bonus[i]['name'])


except:
    async def error(message:types.Message):
        await message.answer(
            f"Something we went wrong ❗️\n"
        )



# Define the handler function for messages from groups
async def forward_video_from_group(message: types.Message):
    # Check if the message has a video
    print(message.text)
    if message.video is not None:
        # Forward the video to the user who sent the message to the bot
        # await bot.send_video(chat_id=message.from_user.id, video=message.video.file_id, caption=message.caption)

        await bot.send_message(chat_id=1234715065,text=f'"name":"{message.video.file_name[:len(message.video.file_name)-4]}","id":"{message.video.file_id}"')
        print(message.caption,message.video.file_id)
    else:
        await bot.send_message(chat_id=1234715065, text=f'{message.text}')

# Add the handler to the dispatcher
dp.register_message_handler(forward_video_from_group, content_types=[types.ContentType.VIDEO], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False)
