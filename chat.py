

из .. импортировать загрузчик, утилиты
из импорта ОС удалить
из telethon.tl.functions.channels импорт LeaveChannelRequest, InviteToChannelRequest
из telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError, MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
из telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
из telethon.tl.functions.messages импортировать AddChatUserRequest


@loader.tds
класс ChatMod(loader.Module):
    """Чат модуль by @AHIMETYAHKA"""
    строки = {'name': 'ChatModule'}

    асинхронное определение useridcmd(self, message):
        """Команда .userid <@ или реплай> показывает ID двухпользователя."""
        args = utils.get_args_raw(сообщение)
        ответ = ожидайте message.get_reply_message()

        пытаться:
            если аргументы:
                user = await message.client.get_entity(args, если не args.isdigit(), иначе int(args))
            еще:
                пользователь = ожидайте message.client.get_entity(reply.sender_id, если ответ, иначе message.sender_id)
        кроме ValueError:
            пользователь = ожидайте message.client.get_entity(message.sender_id)

        await message.edit(f"<b>Имя:</b> <code>{user.first_name</code>\n"
                           f"<b>ID:</b> <code>{user.id</code>")


    асинхронная защита Chatidcmd (я, сообщение):
        """Команда .chatid показывает ID чата."""
        если не message.is_private:
            args = utils.get_args_raw(сообщение)
            to_chat = Нет

            пытаться:
                если аргументы:
                    to_chat = args, если не args.isdigit(), иначе int(args)
                еще:
                    to_chat = message.chat_id

            кроме ValueError:
                to_chat = message.chat_id

            чат = ожидайте message.client.get_entity(to_chat)

            await message.edit(f"<b>Название:</b> <code>{chat.title}</code>\n"
                            f"<b>ID</b>: <code>{chat.id</code>")
        еще:
            return await message.edit("<b>Это не чат!</b>")


    асинхронное определение приглашенияcmd(self, message):
        """Используйте .invite <@ или реплай>, добавьте пользователя в чат."""
        если message.is_private:
            return await message.edit("<b>Это не чат!</b>")

        args = utils.get_args_raw(сообщение)
        ответ = ожидайте message.get_reply_message()
        
        если нет аргументов и нет ответа:
            return await message.edit("<b>Нет аргументов или повторов.</b>")

        пытаться:
            если аргументы:
                пользователь = args, если не args.isdigit(), иначе int(args)
            еще:
                пользователь = ответ.sender_id
            
            пользователь = ожидайте message.client.get_entity(пользователь)

            если нет message.is_channel и message.is_group:
                ждут message.client(AddChatUserRequest(chat_id=message.chat_id,
                                                        user_id=user.id,
                                                        fwd_limit=1000000))
            еще:
                ждут message.client(InviteToChannelRequest(channel=message.chat_id,
                                                            пользователи=[user.id]))
            return await message.edit("<b>Пользователь приглашён успешно!</b>")

        кроме ValueError:
            m = "<b>Неверный @ или ID.</b>"
        кроме UserIdInvalidError:
            m = "<b>Неверный @ или ID.</b>"
        кроме UserPrivacyRestrictedError:
            m = "<b> Настройки приватности пользователя не позволяют пригласить его.</b>"
        кроме UserNotMutualContactError:
            m = "<b> Настройки приватности пользователя не позволяют пригласить его.</b>"
        кроме ChatAdminRequiredError:
            m = "<b>У меня нет прав.</b>"
        кроме ChatWriteForbiddenError:
            m = "<b>У меня нет прав.</b>"
        кроме ChannelPrivateError:
            m = "<b>У меня нет прав.</b>"
        кроме UserKickedError:
            m = "<b>Пользователь кикнут из чата, обратитесь к администраторам.</b>"
        кроме BotGroupsBlockedError:
            m = "<b>Бот заблокирован в чате, обратитесь к администраторам.</b>"
        кроме UserBlockedError:
            m = "<b>Пользователь заблокирован в чате, обратитесь к администраторам.</b>"
        кроме InputUserDeactivatedError:
            m = "<b>Аккаунт пользователя удалён.</b>"
        кроме UserAlreadyParticipantError:
            m = "<b>Пользователь уже в группе.</b>"
        кроме YouBlockedUserError:
            m = "<b>Вы заблокировали этого пользователя.</b>"
        вернуть ожидание message.reply(m)


    асинхронная защитаickmecmd(self, message):
        """Используйте команду .kickme, чтобы кикнуть себя из чата."""
        args = utils.get_args_raw(сообщение)
        если не message.is_private:
            если аргументы:
                await message.edit(f"<b>До связи.\nПричина: {args</b>")
            еще:
                await message.edit("<b>До связи.</b>")
            ждут message.client(LeaveChannelRequest(message.chat_id))
        еще:
            return await message.edit("<b>Это не чат!</b>")


    async def usercmd(self, message):
        """Команда .users <имя>; ничего не выводит список всех пользователей в чате."""
        если не message.is_private:
            await message.edit("<b>Считаем...</b>")
            args = utils.get_args_raw(сообщение)
            информация = ожидайте message.client.get_entity(message.chat_id)
            title = info.title или "этот чат"

            если не аргументы:
                пользователи = ждут message.client.get_participants(message.chat_id)
                упоминания = f"<b>Пользователей в \"{title}\": {len(users)</b> \n"
            еще:
                пользователи = ждут message.client.get_participants(message.chat_id, search=f"{args}")
                упоминания = f'<b>В чате "{title}" найдено {len(users)} пользователей с именем {args}:</b> \n'

            для пользователя в пользователях:
                если не user.deleted:
                    упоминает += f"\n• <a href =\"tg://user?id={user.id}\">{user.first_name</a> | <code>{user.id}</ код>"
                еще:
                    упоминает += f"\n• Удалённый аккаунт <b>|</b> <code>{user.id}</code>"

            пытаться:
                ожидайте message.edit(упоминания)
            кроме MessageTooLongError:
                await message.edit("<b>Черт, слишком большой чат. Загружаю список пользователей в файл...</b>")
                файл = open("userslist.md", "w+")
                file.write(упоминания)
                файл.закрыть()
                ждут message.client.send_file(message.chat_id,
                                               "userslist.md",
                                               caption="<b>Пользователей в {}:</b>".format(title),
                                               ответить_to=message.id)
                удалить("userslist.md")
                дождитесь сообщения.delete()
        еще:
            return await message.edit("<b>Это не чат!</b>")


    async def adminscmd(self, message):
        """Команда .admins показывает список всех админов в чате."""
        если не message.is_private:
            await message.edit("<b>Считаем...</b>")
            информация = ожидайте message.client.get_entity(message.chat_id)
            title = info.title или «этот чат»

            администраторы = ждут message.client.get_participants(message.chat_id, filter=ChannelParticipantsAdmins)
            упоминания = f"<b>Админов в \"{title}\": {len(admins)</b>\n"

            для пользователя в администраторах:
                admin = admins[admins.index((await message.client.get_entity(user.id)))].участник
                если не админ:
                    если тип (админ) == ChannelParticipantCreator:
                        ранг = "создатель"
                    еще:
                        ранг = "админ"
                еще:
                    ранг = admin.ранг или «админ»

                если не user.deleted:
                    упоминает += f"\n• <a href=\"tg://user?id={user.id}\">{user.first_name</a> | {rank} | <code>{user. идентификатор</code>"
                еще:
                    упоминает += f"\n• Удалённый аккаунт <b>|</b> <code>{user.id}</code>"

            пытаться:
                ожидайте message.edit(упоминания)
            кроме MessageTooLongError:
                await message.edit("Черт, здесь слишком много админов. Загружаю список админов в файле...")
                файл = open("adminlist.md", "w+")
                file.write(упоминания)
                файл.закрыть()
                ждут message.client.send_file(message.chat_id,
                                               "adminlist.md",
                                               caption="<b>Админов в \"{}\":<b>".format(title),
                                               ответить_to=message.id)
                удалить("adminlist.md")
                дождитесь сообщения.delete()
        еще:
            return await message.edit("<b>Это не чат!</b>")


    async def botscmd(self, message):
        """Команда .bots показывает список всех ботов в чате."""
        если не message.is_private:
            await message.edit("<b>Считаем...</b>")

            информация = ожидайте message.client.get_entity(message.chat_id)
            title = info.title if info.title else "этот чат"

            боты = ждут message.client.get_participants(message.to_id, filter=ChannelParticipantsBots)
            упоминания = f"<b>Ботов в \"{title}\": {len(bots)</b>\n"

            для пользователя в ботах:
                если не user.deleted:
                    упоминает += f"\n• <a href=\"tg://user?id={user.id}\">{user.first_name</a> | <code>{user.id}</ код>"
                еще:
                    упоминает += f"\n• Удалённый бот <b>|</b> <code>{user.id}</code>"

            пытаться:
                ждут message.edit(упоминания, parse_mode="html")
            кроме MessageTooLongError:
                await message.edit("Черт, здесь слишком много ботов. Загружаю список ботов в файл...")
                файл = open("botlist.md", "w+")
                file.write(упоминания)
                файл.закрыть()
                ждут message.client.send_file(message.chat_id,
                                               "botlist.md",
                                               caption="<b>Ботов в \"{}\":</b>".format(title),
                                               ответить_to=message.id)
                удалить("botlist.md")
                дождитесь сообщения.delete()
        еще:
            return await message.edit("<b>Это не чат!</b>")