import {useNavigate} from "react-router-dom";

import {UserOrders} from "../Orders/UserOrders";



const OfficePage = () => {
    const navigate = useNavigate();
    return (
        <div>
            <button onClick={() => navigate('/office/services')}>Make an Order</button>
            <button onClick={() => navigate('/office/profile')}>Profile</button>
            <UserOrders/>
        </div>
    )
}

export {OfficePage};
