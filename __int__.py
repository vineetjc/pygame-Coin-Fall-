if __name__ == '__main__':
    import sys, subprocess
    dependencies = ['pygame']
    subprocess.call([sys.executable, '-m', 'pip', 'install'] + dependencies)
    import dep_1
    main()
