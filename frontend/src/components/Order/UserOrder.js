import {useNavigate} from "react-router-dom";

import {useDispatch} from "react-redux";
import {orderActions} from "../../redux";

const UserOrder = ({order}) => {

    const navigate = useNavigate();
    const dispatch = useDispatch();

    return (
        <div>
            <div>id:{order.id}</div>
            <div>address:{order.address}</div>
            <div>status:{order.status}</div>


            <button onClick={() => {
                navigate(`/office/order/${order.id}/details`)
                dispatch(orderActions.setOrder(order))
            }}>Details</button>

            <hr/>
        </div>
    )
}
export {UserOrder};
