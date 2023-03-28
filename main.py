from aiogram import Dispatcher , Bot,executor,types
from aiogram.types import reply_keyboard,ReplyKeyboardMarkup
bot_token="6166494743:AAE7Op1Ij5oM_cWVtoDW6OiXZC5_XCNakEE"

bot=Bot(token=bot_token)
dp=Dispatcher(bot)

try:
    menus=[
        ["Modern Java Script"],
        ["React - The Full Course"]
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

    basic_concepts={
        1:{
            "name":"1. Resources ",
            "id":"BAACAgIAAx0CdCu1oAADOGQiqge3bsYqUAWGCboHuRILduw0AAIhLAAC-K4YSRpJZ7Oci09NLwQ"
        },
        2: {
            "name": "2. Java Script in 100 Seconds ",
            "id": "BAACAgIAAx0CdCu1oAADOWQiqlFvH9nLhXfrBd5bX_w7wBoUAAIjLAAC-K4YSdhe5kHFPCrzLwQ"
        },
        3: {
                "name": "3.  JavaScript Crash Course ",
                "id": "BAACAgIAAx0CdCu1oAADOmQiqsdpRzhKqVvoUW_DBwlaS3BrAAItLAAC-K4YSbOWYzt3jUZZLwQ"
            }
    }

    advanced_concepts={
        1:{
            "name": "1. Prototype Chain ",
            "id": "BAACAgIAAx0CdCu1oAADO2QirR7IPdw2fKw7ZHFsb_dfbkhEAAJOLAAC-K4YSTEdd0KeH9WvLwQ"
        },
        2:{
                "name": "2. Destructuring ",
                "id": "BAACAgIAAx0CdCu1oAADPGQirV3RRXRr0p0NTUz99XNkG6T0AAJSLAAC-K4YSVE4gXrVkqY-LwQ"
        },
        3: {
            "name": "3. Spread  ",
            "id": "BAACAgIAAx0CdCu1oAADPWQirYB5CfHSaHTKwb7sAAGnQf-2FwACUywAAviuGEm4aF9gXzL46i8E"
        },
        4: {
            "name": "4. Optional Chaining ",
            "id": "BAACAgIAAx0CdCu1oAADPmQirdilrxrYp0RHGWaH7IPTCqGnAAJYLAAC-K4YSd3VSva4D8UbLwQ"
        },
        5: {
                "name": "5. Nullish Coalescing ",
                "id": "BAACAgIAAx0CdCu1oAADP2QirfLWcSZhMYEVWIn-rNe8wkxCAAJaLAAC-K4YScyj004yxTlzLwQ"
            },
        6: {
                    "name": "6. Higher Order Functions  ",
                    "id": "BAACAgIAAx0CdCu1oAADQGQir8OTmUnwI4RQd_jLOZqRmSj8AAJtLAAC-K4YSQrEJRWsNmxtLwQ"
                },
        7: {
            "name": "7.  Closures ",
            "id": "BAACAgIAAx0CdCu1oAADQWQir_CEDG_GBig2EjdwzHBMv_jmAAJwLAAC-K4YSctomtyND_p7LwQ"
        },
        8: {
                "name": "8. Array Tricks",
                "id": "BAACAgIAAx0CdCu1oAADQmQisAEKpD7qAm5oWT1joupWvWvwAAJxLAAC-K4YScU0nTR3e7FfLwQ"
            },
        9: {
                    "name": "9. History of JavaScript",
                    "id": "BAACAgIAAx0CdCu1oAADQ2QisK209i-6xep4NFzmi1lTV2r0AAJ7LAAC-K4YSaYKjxL4tOMkLwQ"
                }
    }

    algorithms={
        1: {
            "name": "1. Comulative Sum  ",
            "id": "BAACAgIAAx0CdCu1oAADRGQisqWvhuxBgf1hscknnLTL8mCcAAKcLAAC-K4YSffCWHeVEjhuLwQ"
        },
        2: {
            "name": "2. Binary Search ",
            "id": "BAACAgIAAx0CdCu1oAADRWQisr-jxbGTWeRxpzQZZb3eq6RqAAKfLAAC-K4YSX7G-dlj1qosLwQ"
        },
        3: {
            "name": "3. Least Recently Used (LRU) Cache ",
            "id": "BAACAgIAAx0CdCu1oAADRmQisu_y7gckHye3ugcpTAYTUDqVAAKjLAAC-K4YSarLal0N6G-ALwQ"
        },
        4: {
            "name": "4. TDD with Vitest",
            "id": "BAACAgIAAx0CdCu1oAADR2QisxWJLLx_KD2H3Zlednl8gdxwAAKlLAAC-K4YSXNMKVisLB-GLwQ"
        }
    }
    dream_app={
        1: {
            "name": "1. Initial Setup ",
            "id": "BAACAgIAAx0CdCu1oAADSGQitEZ8Abm3Z9O781QggRnCyucRAAK6LAAC-K4YSfDfqpjfWhHvLwQ"
        },
        2: {
            "name": "2. RESTful APIs ",
            "id": "BAACAgIAAx0CdCu1oAADSWQitHD43DQMElzTVvFfiaAzDyFaAAK8LAAC-K4YSeSoeXWwxgABpi8E"
        },
        3: {
            "name": "3. Text-to-Image Server ",
            "id": "BAACAgIAAx0CdCu1oAADSmQitKa1BiZKMQLwRMDFO9bxEEHgAALALAAC-K4YSaNexrnyn_kjLwQ"
        },
        4: {
            "name": "4. Rest Client	",
            "id": "BAACAgIAAx0CdCu1oAADS2QitLmzvqx4EhmsXBp_SreiqbArAALBLAAC-K4YSclSbNmYggY4LwQ"
        },
        5: {
            "name": "5. Text-to-Image Frontend UI ",
            "id": "BAACAgIAAx0CdCu1oAADTGQitOvRmuUpLF_H1PRtU77tFgT0AALCLAAC-K4YSQ3iqOm_fPzALwQ"
        },
        6: {
            "name": "6. Loading Spinner ",
            "id": "BAACAgIAAx0CdCu1oAADTWQitQiwD-n5cg8LmiQj4gOPV9TWAALDLAAC-K4YSSzilzcNm7OgLwQ"
        },
        7: {
            "name": "7. Error Handling ",
            "id": "BAACAgIAAx0CdCu1oAADTmQitUM6b2qi_WgY8tQREnQfj3RVAALELAAC-K4YSZNSAbjfWl-uLwQ"
        }
    }
    react_rp_keyboard=[
        ["Part 1"],
        ["Part 2"],
        ["Animal Farm"],
        ["🔙Back"]
    ]


    part_1={
        1: {
            "name": "1. React in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADUWQivPBZilB6zhvoJI38THjOJ0q0AAL_LAAC-K4YSaYFzgH1fV1fLwQ"
        }, 
        2: {
            "name": "2. Anatomy",
            "id": "BAACAgIAAx0CdCu1oAADVGQivXN0yYviQfVmPwbhRMPxNqdkAAMtAAL4rhhJw71SCuDBXlgvBA"
        },
        3: {
            "name": "3.Components",
            "id": "BAACAgIAAx0CdCu1oAADVWQiyQk6-RBszxwnenCC5wAB5m9vWgACei0AAviuGEm6ikDSa7O_Gy8E"
        },
        4: {
            "name": "4. Conditional Rendering ",
            "id": "BAACAgIAAx0CdCu1oAADVmQiySGRmCYCOvcNHVHM9GfUujnHAAJ-LQAC-K4YSbIvzZez9Y4FLwQ"
        },
        5: {
            "name": "5. Loops",
            "id": "BAACAgIAAx0CdCu1oAADV2QiyS8GJYEaQh69QGQz4F4UyYKvAAKBLQAC-K4YST03RxZuWPgYLwQ"
        },
        6: {
            "name": "6.Events",
            "id": "BAACAgIAAx0CdCu1oAADWGQiyUZ38UEl9gKvNo4TTDPmB_-FAAKELQAC-K4YSUMHEzts0A6kLwQ"
        },
        7: {
            "name": "7. State",
            "id": "BAACAgIAAx0CdCu1oAADWWQiynMAASX97C4PEujX9TAmd9RyzAACji0AAviuGEmOX7VlRwEF9y8E"
        },
        8: {
            "name": "8. Lifecycle and Effects",
            "id": "BAACAgIAAx0CdCu1oAADWmQiyoIkCRRomiSGkWhcS23GxbsZAAKQLQAC-K4YSQffNYDEVVwjLwQ"
        }   
    }

    part_2={
        1: {
            "name": "9. Context ",
            "id": "BAACAgIAAx0CdCu1oAADW2QiywiMt8cLyBG4AfAtApfg2WndAAKTLQAC-K4YSfuEfbY6Ejp3LwQ"
        }, 
        2: {
            "name": "10. Error Boundries",
            "id": "BAACAgIAAx0CdCu1oAADXGQiyxNkqTR9kpeqKiMsMZUTrDeuAAKULQAC-K4YSaX7K_e1leS8LwQ"
        },
        3: {
            "name": "11. Next.js in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADXWQiy0Ia-AdPE86vO9u-oqnbu1YiAAKWLQAC-K4YSQ2i2RRpQr0eLwQ"
        },
        4: {
            "name": "12. Prisma in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADXmQiy18lnwRaMDOm5c1sCr0QZB6eAAKXLQAC-K4YSVWcwIi5-aDFLwQ"
        },
        5: {
            "name": "13. Vite in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADX2Qiy5sP1hNIEAAB9n2QiqjJKiTZmAACmC0AAviuGElDCNgL48g6bC8E"
        },
        6: {
            "name": "14. React Query in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADYGQiy8Dn4g_5uHKTtZd4mlau24hHAAKZLQAC-K4YSUpO3rxFUtSjLwQ"
        },
        7: {
            "name": "15. Progressive Web Apps in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADYWQiy-q_UZTSuuvcGjOjz_CdzWP0AAKaLQAC-K4YSeX3sSWCaEH7LwQ"
        },
        8: {
            "name": "16. Redux in 100 Seconds",
            "id": "BAACAgIAAx0CdCu1oAADYmQiy_v0CCCGCI8gQMUP8vRJSuncAAKbLQAC-K4YSXw4YtIRx2ZMLwQ"
        }   
    }

    animal_farm={
        1: {
            "name": "1. Setup ",
            "id": "BAACAgIAAx0CdCu1oAADY2QizOBJFhRev9i73szWW7eEXnKeAAKgLQAC-K4YSTW1wzl48trCLwQ"
        },
        2: {
            "name": "2. Express Server",
            "id": "BAACAgIAAx0CdCu1oAADZGQizP0Br8_OCvCgeXR0hlnFu2iWAAKjLQAC-K4YSYItSgI9HbHBLwQ"
        },
        3: {
            "name": "3. Search Frontend",
            "id": "BAACAgIAAx0CdCu1oAADZWQizSxIY5b7rzEsvpakb_tsTqRlAAKkLQAC-K4YSQrhipZWus8aLwQ"
        } 
    }



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

except:
    async def error(message:types.Message):
        await message.answer(
            f"Something we went wrong ❗️\n"
        )





if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False)