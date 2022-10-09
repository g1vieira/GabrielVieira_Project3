import arcade
my_window = arcade.open_window(500, 500, "First Window")
arcade.start_render()

arcade.draw_circle_outline(187.5, 187.5, 31.25, arcade.color.WINE)
arcade.draw_circle_outline(312.5, 187.5, 31.25, arcade.color.WINE)
arcade.draw_line(125, 187.5, 156.25, 187.5, arcade.color.WINE)
arcade.draw_line(343.75, 187.5, 375, 187.5, arcade.color.WINE)
arcade.draw_line(218.75, 187.5, 281.25, 187.5, arcade.color.WINE)
arcade.draw_arc_outline(250, 183, 250, 187.5, arcade.color.WINE, 0, 180, 1)
arcade.draw_triangle_outline(62.5, 250, 93.75, 375, 125, 250, arcade.color.WINE)


arcade.finish_render()




arcade.run()