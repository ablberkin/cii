### Background

一个基于Vue和Python的校园信息小程序，目的是为了更好地服务本校学术，针对当下校园的痛点问题进行针对性解决。主要功能包括信息发布和交流，试图解决当下校园信息存在信息差的现象，部分信息较难获取，从而设立一个专门的小程序实现信息的分类和汇总。小程序相对于传统的网页端论坛而言更加轻便、便于移动时代的用户使用；相对于app而言，无需占用太多手机空间，增强用户使用的意愿。

### Install

- 前端项目使用uniapp框架，用HbuilderX 3.3.13作为IDE。需要提前安装node，npm
- 后端项目使用了Django框架，需要配置python的虚拟环境，包括Django，django-rest-framework等依赖环境

```
python -m venv 文件夹名称 #虚拟环境
pip install django
pip install djangorestframework #安装依赖环境
pip install django-cors-headers #跨域问题
pip install psycopg2

pip install markdown       # 对可浏览 API 的 Markdown 支持。
pip install django-filter  # 过滤支持
pip install pygments  # 用于代码高亮
```

- 使用PostgreSQL作为数据库，需要提前进行安装配置

### Usage

#### frontend

- 保存前端文件的位置

- pages-mine-mine：“我的”界面；pages-mine-register：“注册”，现阶段仅支持邮箱注册，上传到PostgreSQL进行保存；pages-mine-login：“登录”      `注：pages-mine-mine代表路径，相应文件处在frontend-pages-mine-mine的位置`

![image-20220427215713853](C:\Users\Albertjin\AppData\Roaming\Typora\typora-user-images\image-20220427215713853.png)

- pages-index-index：“首页”，对各种信息进行分类导航；pages-index-newsindex：校园讯息展示；pages-index--newsDetail：讯息详情浏览
- editor-schoolNewsEditor：“文本编辑器”，实现了富文本编辑器的前后端联通，文本信息上传到本地PostgreSQL服务器，图片资源借助uniapp的unicloud特性，上传到阿里云数据库上

![image-20220427215611490](C:\Users\Albertjin\AppData\Roaming\Typora\typora-user-images\image-20220427215611490.png)

#### backend

- 保存后端文件的位置
- backend：项目的配置，包括路由、app的注册……
- newsindex：校园讯息的数据库模型
- users：用户的数据库模型
- emailValidate：邮箱验证，负责验证码保存与核对

### TODO

- 前端界面的完善和美化，完善报错功能
- 后端逻辑的完善：实现讯息搜索的功能，计划使用Haystack+Whoosh
- 数据库的迁移：一部分功能迁移到NoSQL数据库上，优化性能