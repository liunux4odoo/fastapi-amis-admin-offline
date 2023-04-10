import fastapi
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from functools import lru_cache
from string import Template


BASE_DIR = Path(__file__).resolve().parent


def patch_offline(
    app,
    static_url='/static/offline',
):
    # 1. local static files
    app.mount(static_url,
              StaticFiles(directory=BASE_DIR / 'static'), static_url.replace('/', '-'))

    # 2.配置 Swagger UI
    def custom_swagger_ui_html(*args, **kw):
        kw.update({
            'swagger_js_url': f'{static_url}/openapi/swagger-ui-bundle.4.14.0.js',
            'swagger_css_url': f'{static_url}/openapi/swagger-ui.4.14.0.css',
            'swagger_favicon_url': f'{static_url}/swagger_icon.ico',
        })
        return fastapi.openapi.docs.get_swagger_ui_html(*args, **kw)
    fastapi.applications.get_swagger_ui_html = custom_swagger_ui_html

    # 3.配置 redoc UI
    def custom_redoc_html(*args, **kw):
        kw.update({
            'redoc_js_url': f'{static_url}/openapi/redoc@2.0.0-rc.66.standalone.js',
            'redoc_favicon_url': f'{static_url}/redoc_icon.ico',
        })
        return fastapi.openapi.docs.get_redoc_html(*args, **kw)
    fastapi.applications.get_redoc_html = custom_redoc_html

    # 4. 配置amis模板
    try:
        import fastapi_amis_admin
        amis = fastapi_amis_admin.amis
        templates_dir = BASE_DIR / 'templates'
        amis.components.Page.__default_template_path__ = templates_dir / 'amis_page.html'
        amis.components.App.__default_template_path__ = templates_dir / 'amis_app.html'

        @lru_cache
        def custom_amis_templates(*args, **kw):
            template = amis.utils.amis_templates(*args, **kw)
            return Template(template.safe_substitute(static_url=static_url))

        amis.components.amis_templates = custom_amis_templates
    except ImportError:
        pass
