from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    print('------ PLAYS IN -------')

    matcher = (
        query
        .playsIn("NYR")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

    print('------ HAS AT LEAST, HAS FEWER THAN -------')

    matcher2 = (
        query
        .playsIn("NYR")
        .hasAtLeast(5, "goals")
        .hasFewerThan(10, "goals")
        .build()
    )

    for player in stats.matches(matcher2):
        print(player)

    print('------ OR -------')

    matcher3 = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            query.playsIn("EDM")
            .hasAtLeast(40, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher3):
        print(player)


if __name__ == "__main__":
    main()
