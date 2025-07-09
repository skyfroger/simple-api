import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
import io

from typing import Annotated
from fastapi import APIRouter, Response, Query

router = APIRouter(tags=["QR-код"])


@router.get(
    "/qr",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
    summary="QR-код по тексту",
)
def create_qr_code(text: Annotated[str, Query(title="Текст", max_length=256)]):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        fill_color="black",
        back_color="white",
    )

    buf = io.BytesIO()
    img.save(buf, format="png")
    byte_im = buf.getvalue()

    return Response(content=byte_im, media_type="image/png")
