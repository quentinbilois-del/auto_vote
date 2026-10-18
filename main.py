
from playwright.sync_api import sync_playwright

URL = "https://topmoddedservers.com/serveur/create-france/vote"

PSEUDOS = [
    "Loloaze",
    "ZipZap38",
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            for pseudo in PSEUDOS:
                if not 3 <= len(pseudo) <= 16:
                    print(f"Pseudo invalide : {pseudo}")
                    continue

                print(f"\nVérification du pseudo : {pseudo}")

                page.goto(
                    URL,
                    wait_until="domcontentloaded",
                    timeout=60000,
                )

                champ = page.locator("#username")
                champ.wait_for(state="visible", timeout=15000)
                champ.fill(pseudo)
                print("Valeur saisie :", champ.input_value())

                bouton = page.get_by_role("button", name="Confirmer mon vote")

                print("Bouton désactivé :", await_not_used if False else bouton.is_disabled())
                print("Champ visible :", champ.is_visible())
                print("Messages affichés :")
                print(page.locator("body").inner_text()[:4000])
                bouton.click()

                # Attendre que la page ait terminé sa navigation éventuelle
                page.wait_for_load_state("domcontentloaded", timeout=15000)

                # Afficher le résultat
                page.wait_for_timeout(1500)
                print("Résultat affiché :")
                print(page.locator("body").inner_text()[:3000])

        except Exception as erreur:
            print("Erreur Playwright :", erreur)

        finally:
            browser.close()


if __name__ == "__main__":
    main()
