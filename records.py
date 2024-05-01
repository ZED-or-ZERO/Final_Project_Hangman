import json

from setting import *

class Records:
    def __init__(self):
        pass 

    def load_scores(self):
        try:
            with open("scores.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_scores(self, scores):
        with open("scores.json", "w") as f:
            json.dump(scores, f)

    def show_high_scores(self, game):
        scores = self.load_scores()
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        game.win.fill(WHITE)
        title_text = game.fonts[2].render("High Scores", 1, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 80))
        game.win.blit(title_text, title_rect)

        y = 150
        for name, score in sorted_scores:
            score_text = game.fonts[1].render(f"{name}: {score}", 1, BLACK)
            score_rect = score_text.get_rect(topleft=(50, y))
            game.win.blit(score_text, score_rect)
            y += 50

        back_text = game.fonts[1].render("Back", 1, BLACK)
        back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT - 80))
        game.win.blit(back_text, back_rect)

        pg.display.update()

        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(pg.mouse.get_pos()):
                        waiting = False

    def get_player_name(self, game):
        name = ""
        font = game.fonts[1]
        input_rect = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        return name
                    elif event.key == pg.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            game.win.fill(WHITE)
            text_surface = font.render(name, True, BLACK)
            game.win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            pg.draw.rect(game.win, BLACK, input_rect, 2)
            pg.display.update()

    def update_high_scores(self, game):
        if not game.won:
            return
        name = self.get_player_name(game)
        if name == "":
            return
        scores = self.load_scores()
        current_score = len(game.word) - game.hangman_status 
        if name not in scores or current_score > scores[name]:
            scores[name] = current_score
            self.save_scores(scores)