import random

class Sidewinder:
    @staticmethod
    def on(grid):
        for row in grid.each_row():
            run = []

            for cell in row:
                run.append(cell)

                at_east_boundary = cell.east is None
                at_north_boundary = cell.north is None
                should_close_out = at_east_boundary or (not at_north_boundary and random.choice([True, False]))

                if should_close_out:
                    member = random.choice(run)
                    if(member.north):
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
                    