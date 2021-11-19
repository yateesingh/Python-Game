# Python-Game
# Problem Description

- This project uses the pygame module to develop a basic game  . The game’s protagonist – Mario can be moved left and right using the respective arrow keys. The main objective of the game is to dodge or kill the opponent (Goombas) .The player is awarded one point for dodging the opponent and five points for destroying the opponent. The player can dodge the opponent by pressing the space bar and jumping over it or kill the enemy by jumping onto the Goombas. The speed of the goombas increase as you score more points thus increasing the difficulty level as you progress in the game. Once you fail to duck the enemy the game is over.
 
## Python Modules Used:
- ●	Pygame
- ●	Random
- ●	Sys
## The important functions in the program:
- 1.	def enemy_maker(enemy_list):  Creates a list which contains the position of each enemy in the game.
- 2.	def draw_enemies(enemy_list,enemy_image): Inserts the image of the enemy at the enemy position.
- 3.	def move_enemies(enemy_list,score): Updates the position of the enemy.
- 4.	def collision(player_pos,enemy_pos): Checks for the collision of the player and the enemy.
- 5.	def cloud_maker(cloud_list): Add some aesthetic value to the game .The function makes a list containing position of clouds , inserts the image and updates its position .
