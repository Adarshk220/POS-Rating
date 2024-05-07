/** @odoo-module */

import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { patch } from "@web/core/utils/patch";

patch(ProductCard.prototype, {

    setup() {
        this.pos = usePos();
        console.log(this.pos,'hello')
         const props = {
            ...super.props,
            product_rating: { type: String, optional: true }
        };
    },

});