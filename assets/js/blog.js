blog = document.getElementById("blog");
blogResponse=""
server = "http://127.0.0.1:8000"
var currentIdx
var Data = {
    titles: {
        titlesJSON: {},
        keys: [],
        fetch: function() {
            m.request({
                    method: "POST",
                    url: server+"/blog/all/",
                    data: { 'field':'titles' }
                })
                .then(function(result) {

                    Data.titles.titlesJSON = JSON.parse(result);
                    console.log(result)
                    Data.titles.keys = Object.keys(Data.titles.titlesJSON);
                    // m.redraw()
                })
        }
    },
    post: {
        body: {},
        fetch: function() {
            m.request({
                    method: "POST",
                    url: server+"/blog/all/",
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
            m('.parallax',m("h1", { class: "title" }, blogResponse.title)),
            m(".", m.trust(markdown.toHTML(blogResponse.body)))
        )):m('')
    }
}

// titles = {
//     oninit: Data.titles.fetch,
//     view: function() {

//         return m('.demo-card-square mdl-card mdl-shadow--2dp',
//             m('.mdl-card__title mdl-card--expand',
//                 Data.titles.keys.length > 0 ? Data.titles.keys.map(function(key) {
//                     return m('h2.mdl-card__title-text', {
//                          onmouseover: function() {
//                                 console.log(Data.titles.titlesJSON[key].title)

//                          },
//                         onclick: function() {
//                             console.log(key)
//                             currentIdx=key;
//                             m.mount(document.body, blogComponent)
//                         }
//                     }, m('.major.blogTitles',
                        
//                         Data.titles.titlesJSON[key].title))

                    
//                 }) : m('')
//             ))

titles = {
    oninit: Data.titles.fetch,
    view: function() {  


         return Data.titles.keys.length > 0 ? Data.titles.keys.map(function(key) {
            return m('.demo-card-square.mdl-card mdl-shadow--2dp',
                    m('.mdl-card__title mdl-card--expand',
                        m('h6.mdl-card__title-text',Data.titles.titlesJSON[key].title)),
                    m('.mdl-card__supporting-text','Lorem ipsum dolor sit amet, consectetur adipiscing elit.Aenan convallis.',
                        m('.date',Data.titles.titlesJSON[key].modifiedDate)),
                    m('.mdl-card__actions mdl-card--border',
                        m('a.mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect',{
                             onclick: function() {
                            console.log(Data.titles.titlesJSON[key].id)
                            currentIdx=Data.titles.titlesJSON[key].id;
                             m.mount(document.body, blogComponent)
                        }

                        },'View')
                        )
                )
         }):m('','nothing')

    }
}

m.mount(blog, titles)