if __name__ == '__main__':
    import sys, subprocess
    dependencies = ['pygame'] # to add furture dependencies
    subprocess.call([sys.executable, '-m', 'pip', 'install'] + dependencies)
    import pygame
    main()
