<template>
    <div class="mb-6 flex items-center justify-between">
                   <div class="flex items-center space-x-6">
                       <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh2ibh9YBLzRs29v8VE96dT1ow0TTfys_gAw&usqp=CAU" class="w-[40px] rounded-full">
                       <p>
                           <strong>
                               <RouterLink :to="{name: 'profile', params:{'id': comment.created_by.id}}">{{ comment.created_by.name }}</RouterLink>
                           </strong>
                       </p>
                   </div>
                   <p class="text-gray-600">{{ comment.created_at_formatted }} ago</p>
               </div>
               <p>{{ comment.body }}</p>
            

</template>

<script>

import axios from 'axios';
import { RouterLink } from 'vue-router';

export default (await import('vue')).defineComponent({
   props: {
       comment: Object
   },

   components: { RouterLink }
})

</script>