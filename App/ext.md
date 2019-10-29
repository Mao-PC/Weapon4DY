# Flask_migrate 插件

- 迁移插件

使用流程:
- 安装: pip install Flask_migrate
- 使用:
    - flask db 命令
        - init
        - migrate
        - upgrade
    - 结合 flask-script 使用:
        - 在manager上添加管理指令 `manager.add_command('db', MigrateCommand)`
        - python manager db [指令]