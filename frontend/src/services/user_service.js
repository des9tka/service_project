import {axiosService} from "./axios_service";
import {urls, userAttr} from "../configs";

const user_service = {
    getAll: () => axiosService.get(urls.USERS),
    getSelf: () => axiosService.get(`${urls.USERS}${userAttr.self}`),
    getOrders: (page= 1, status= 1) => axiosService.get(`${urls.USERS}${userAttr.orders}`, {params: {page, status}}),
    getById: (id) => axiosService.get(`${urls.USERS}/${id}`),
    newOrder: (order) => axiosService.post(`${urls.USERS}${userAttr.new_order}`, order),
    changeService: (service_id) => axiosService.patch(`${urls.USERS}${userAttr.change_service}${service_id}`),
    change_employee_service: (user_id, service_id) => axiosService.patch(urls.USERS, user_id, userAttr.change_employee_service, service_id),
    activate: (id) => axiosService.patch(`${urls.USERS}/${id}${userAttr.activate}`),
    deactivate: (id) => axiosService.patch(`${urls.USERS}/${id}${userAttr.deactivate}`),
    toAdmin: (id) => axiosService.patch(`${urls.USERS}/${id}${userAttr.to_admin}`),
    toEmployee: (id) => axiosService.patch(`${urls.USERS}/${id}${userAttr.to_employee}`),
    toUser: (id) => axiosService.patch(`${urls.USERS}/${id}${userAttr.to_user}`),
    profileUpdate: (profile) => axiosService.patch(`${urls.USERS}${userAttr.profile_update}`, profile),
    addPhoto: (photo) => axiosService.patch(`${urls.USERS}${userAttr.add_photo}`, {user_photo: photo})
}

export {
    user_service
}