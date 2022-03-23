import asyncio
import genshin

async def main():
    client = genshin.GenshinClient()
    cookies = genshin.get_browser_cookies()
    client.set_cookies(cookies)

    notes = await client.get_notes(901211014)
    time = notes.until_resin_recovery
    hours, minutes = divmod(time // 60, 60)
    print(f"Current resin: {notes.current_resin}/{notes.max_resin}")
    print(f"Resin full in {hours:.0f} hours {minutes:.0f} minutes")
    print(f"Comissions left: {notes.completed_commissions}/{notes.max_comissions}")
    print(f"Current realm currency: {notes.current_realm_currency}/{notes.max_realm_currency}")
    print(f"Expeditions finished: {sum(expedition.finished for expedition in notes.expeditions)}")

    await client.close()

asyncio.run(main())
