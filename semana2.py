import streamlit as st

def main():
    st.title('Hello World')
    #comandos interativos
    st.markdown('Botao')
    botao = st.button('Botao')
    if botao:
        st.markdown('Clicado')

    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicado')

    st.markdown('Radio')
    radio = st.radio('Escolha as opcoes', ('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')

    st.markdown('SelectBox')
    select = st.selectbox('Escolha uma opção', ('...','Opt 1', 'Opt 2'))
    if select == 'Opt 1':
        st.markdown('Opt 1')
    if select == 'Opt 2':
        st.markdown('Opt 2')

    st.markdown('MultiSelect')
    multi = st.multiselect('Escolha :', ('Opt 1', 'Opt 2'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 2':
        st.markdown('Opt 2')

    st.markdown('File uploader')
    file = st.file_uploader('Choose your file', type = 'csv')
    if file is not None:
        st.markdown('Não está vazio!')
    

if __name__ == '__main__':
    main()