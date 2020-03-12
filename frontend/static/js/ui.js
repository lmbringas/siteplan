const main = async  ()  => {
    let r = await fetch('api/v1/task/1');

    let data = await r.json();
    const container = document.querySelector('#container');

    //classList.add("mystyle");

    const create_task = (name) => {
        const task =  document.createElement("div").classList.add('child');
        const title = document.createElement('span');
        title.textContent = name;
        task.appendChild(title);
        return task;
    }

    const create_tree = (parent, tasks) => {
        let child = false;
        for (i in tasks){
            console.log(tasks[i])
            if (tasks[i].sub_task.length > 0) { // it has children
                child = true;
            } else {
                parent.appendChild(create_task(tasks[i].name))
            }
        }

        if(child) {
            const parent_child =  document.createElement("div").classList.add('section');
            for (i in tasks){
                create_tree(parent_child, task[i].sub_task)    
            }
            parent.appendChild(parent_child);
            
        }

    }

    create_tree(container,data);
}

main();
