
from lecture.wolnelektury.service.WolneLekturyService import \
    WolneLekturyService


def main():

    WolneLekturyService.load_lecture_by_author_slug('adam-mickiewicz')


if __name__ == "__main__":
    main()
