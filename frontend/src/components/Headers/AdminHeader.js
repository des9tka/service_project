import {NavLink} from "react-router-dom";

const AdminHeader = () => {

    return (
        <div className={'header'}>
            <NavLink to={'home'}>Home</NavLink>
            <NavLink to={'users'}>Users</NavLink>
            <NavLink to={'orders'}>Orders</NavLink>
            <NavLink to={'about'}>About</NavLink>
            <NavLink to={'/auth'}>Exit</NavLink>
        </div>
    )
}
export {
    AdminHeader
};
