#!/usr/bin/env python3
import voting


if __name__ == '__main__':
    voting.db.create_all()
    voting.app.run()

