
#主要实现用户的增删改查

from api.base import Base


class USerManager(Base):

    def __init__(self):
        self.add_user_url= self.get_url('/admin/admin/create')
        self.edit_user_url = self.get_url('/admin/admin/update')
        self.search_user_url = self.get_url('/admin/admin/list?page=1&limit=20&sort=add_time&order=desc')
        self.delete_user_url = self.get_url('/admin/admin/delete')


    #新增用户管理员
    def add_user(self,username,password,**kwargs):
        """
        请求的是添加管理员的接口
        :return: 添加管理员的接口返回的json数据
        """
        user_data = {'username':username,'password':password}
        if kwargs:
            logger.info("添加管理员可选参数:{}",**kwargs)
            user_data.update(**kwargs)
        return self.post(self.add_user_url,user_data)

    #查询管理员
    def search_user(self):

        return self.get(self.search_user_url)

    #修改管理员
    def edit_user(self,id,username,password,**kwargs):
        """
        请求的是修改管理员接口

         :return:修改管理员的返回的json数据
         """
        user_data = {'id': id, 'username': username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
        return self.post(self.edit_user_url, user_data)

    #删除管理员
    def delete_user(self,id,username,**kwargs):
        """
        请求的是删除管理员接口

        :return:删除管理员的返回的json数据
        """
        user_data = {'id':id,'username':username}
        if kwargs:
           user_data.update(**kwargs)
        return self.post(self.delete_user_url,user_data)


