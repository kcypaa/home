blog = document.getElementById("blog");
blogResponse=""
var currentIdx
var Data = {
    titles: {
        titlesJSON: {},
        keys: [],
        fetch: function() {
            m.request({
                    method: "POST",
                    url: "http://127.0.0.1:8000/blog/all/",
                    data: { 'field':'titles' }
                })
                .then(function(result) {

                    Data.titles.titlesJSON = JSON.parse(result);
                    Data.titles.keys = Object.keys(Data.titles.titlesJSON);
                })
        }
    },
    post: {
        body: {},
        fetch: function() {
            m.request({
                    method: "POST",
                    url: "http://127.0.0.1:8000/blog/all/",
                    data: { 'field':'post','idx':currentIdx }
                })
                .then(function(result) {
                    
                    blogResponse = JSON.parse(result);
                    
                    // Data.titles.titlesJSON = JSON.parse(result);
                    // Data.titles.keys = Object.keys(Data.titles.titlesJSON);
                })
        }
    }
}

blogComponent = {
    oninit:Data.post.fetch,

    view: function() {
     

        return (blogResponse!="")?m("main.blog", m('',
            m("h1", { class: "title" }, "My first app"),
            m(".", m.trust(markdown.toHTML(blogResponse.body)))
        )):m('')
    }
}

titles = {
    oninit: Data.titles.fetch,
    view: function() {

        return m('.gallery',
            m('.group.span-' + parseInt(Data.titles.keys.length),
                Data.titles.keys.length > 0 ? Data.titles.keys.map(function(key) {
                    return m('.image.filtered.span-1-5', {
                         onmouseover: function() {
                                console.log(Data.titles.titlesJSON[key].title)

                         },
                        onclick: function() {
                            console.log(key)
                            currentIdx=key;
                            m.mount(document.body, blogComponent)
                        }
                    }, m('.major.blogTitles',
                        
                        Data.titles.titlesJSON[key].title))

                    
                }) : m('')
            ))


    }
}

m.mount(blog, titles)